from __future__ import print_function
import os.path
import base64
import re
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


# If modifying these scopes, delete the file token.json.  
SCOPES = 'https://mail.google.com/'

def getCredentials():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])
    return creds

def unpack_payload(txt):
    """
    use to catch emails fields in payload2fields function
    for mimeType "text/plain" and "text/html"
    """
    recipient, sender, subject = '','',''
    for n in range(len(txt['payload'].get('headers'))):

        if txt['payload'].get('headers')[n]['name'] == 'To':
            recipient = txt['payload'].get('headers')[n]['value']

        if txt['payload'].get('headers')[n]['name'] == 'From':
            sender = txt['payload'].get('headers')[n]['value']

        if txt['payload'].get('headers')[n]['name'] == 'Subject':
            subject = txt['payload'].get('headers')[n]['value']
        return recipient, sender, subject

def payload2fields(txt):
    """
    Transform request GMail API to ready-to-use for emails app.
    """
    #MIME errors management and capture message data
    mimeType = txt['payload'].get('mimeType')
    data, recipient, sender, subject = '', '', '', ''

    if mimeType == "text/plain":
        try:
            recipient, sender, subject = unpack_payload(txt)
            data = txt['payload'].get('body')['data']
        except KeyError:
            print("Error in txt['payload'].get('body')['data']")
            exit()

    elif mimeType == "text/html":
        try:
            recipient, sender, subject = unpack_payload(txt)
            data = txt['payload']['body']['data']

        except IndexError:
            print("Error")
            exit()

    elif mimeType == 'multipart/alternative':
        try:
            for n in range(len(txt['payload']['headers'])):
                if txt['payload']['headers'][n]['name']== 'From':
                    sender = txt['payload']['headers'][n]['value']

                elif txt['payload']['headers'][n]['name']== 'Subject':
                    subject = txt['payload']['headers'][n]['value']

                elif txt['payload']['headers'][n]['name']== 'To':
                    recipient = txt['payload']['headers'][n]['value']

                data =txt['payload']['parts'][0]['body']['data']

        except IndexError:
            print("Error")
            exit()
    
    elif mimeType == 'multipart/mixed':
        try:
            for n in range(len(txt['payload']['headers'])):
                if txt['payload']['headers'][n]['name']== 'From':
                    sender = txt['payload']['headers'][n]['value']
                elif txt['payload']['headers'][n]['name']== 'Subject':
                    subject = txt['payload']['headers'][n]['value']
                elif txt['payload']['headers'][n]['name']== 'To':
                    recipient = txt['payload']['headers'][n]['value']
            data = ''
        except IndexError:
            print("Error")
            exit()

    else:
        print(">>> bad mimeType : need text/plain, text/html, multipart/alternative or multipart/mixed")

    #email fields searching
    for n in range(len(txt['payload'].get('headers'))):

        if txt['payload'].get('headers')[n]['name'] == 'To':
            recipient = txt['payload'].get('headers')[n]['value']

        if txt['payload'].get('headers')[n]['name'] == 'From':
            sender = txt['payload'].get('headers')[n]['value']

        if txt['payload'].get('headers')[n]['name'] == 'Subject':
            subject = txt['payload'].get('headers')[n]['value']

    return sender, recipient, subject, data

def cleanFieldsEmails(sender, recipient, subject, data):
    """
    clean emails field function
    """
    decode = str(base64.urlsafe_b64decode(data))
    message = decode.strip("b'").split("\\r\\n")

    sender = re.findall('\S+@\S+', sender)
    sender = str(sender).strip("['<").strip(">']")

    recipient = re.findall('\S+@\S+', recipient)
    recipient = str(recipient).strip("['<").strip(">']")

    message = message[0]

    return sender, recipient, subject, message

def getMail():
    """
    setup all previous function to get all emails in user mailbox
    """
    creds = getCredentials()
    service = build('gmail', 'v1', credentials=creds)

    
    #Catch email from Gmail, with maxResults parameter and  q = 'subject:*filter*' if necessary
    result = service.users().messages().list(maxResults=100, userId='me').execute()
    messages = result.get('messages')

    if messages != None : 
        count = 0
        for msg in messages:
                count += 1
                print(count)
                txt = service.users().messages().get(userId='me', id=msg['id']).execute()
                email_id = txt['id']
                sender, recipient, subject, data = payload2fields(txt)
                sender, recipient, subject, message = cleanFieldsEmails(sender, recipient, subject, data)
                
    else :
        email_id, sender, recipient, subject, message = "","No emails!"," "," "," "

    return email_id, sender, recipient, subject, message