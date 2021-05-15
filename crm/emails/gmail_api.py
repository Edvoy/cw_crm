from __future__ import print_function
import os.path
import base64
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import re

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
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
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
    use to catch emails fields in payload2fields function for mimeType "text/plain" and "text/html"
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
            recipient = txt['payload']['headers'][0]['value']
            sender = txt['payload']['headers'][1]['value']
            subject = txt['payload']['headers'][20]['value']
            data = txt['payload']['body']['data']

        except IndexError:
            print("Error")
            exit()

    #todo : gérer le multipart alternative et mixed
    # elif mimeType == "multipart/alternative":
    #     try:
    #         data = txt['payload'].get('parts')[0]['body']['data']
    #         recipient, sender, subject = unpack_payload(txt)
    #     except IndexError:
    #         print("Error, list index out of range in get('parts')")
    #         exit()


    # elif mimeType == "multipart/mixed":
    #     recipient = txt['payload']['headers'][0]['value']
    #     sender = txt['payload']['headers'][1]['value']
    #     subject = txt['payload']['headers'][13]['value']
    #     data = 

    else:
        print(">>> bad mimeType, need text/plain, text/html")        

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
    #todo : clean avec du regex

    #regex pattern
    email_pattern = "(?:[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|\"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\\\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])"
    message_pattern = ""

    #clean message
    decode = str(base64.urlsafe_b64decode(data))
    message = decode.strip("b'").split("\\r\\n")

    sender = re.match(email_pattern, sender)
    recipient = re.match(email_pattern, recipient)
    subject = re.match(message_pattern, subject)
    message = message[0]

    return sender, recipient, subject, message

def getMail():
    """
    Shows basic usage of the Gmail API. Ready2Use from google. see link at the top
    """
    creds = getCredentials()
    service = build('gmail', 'v1', credentials=creds)

    # catch email from Gmail, with maxResults parameter and  q = 'subject:*filer*'
    result = service.users().messages().list(maxResults=100, userId='me').execute()
    messages = result.get('messages')

    if messages != None : 
        for msg in messages:
                txt = service.users().messages().get(userId='me', id=msg['id']).execute()
                sender, recipient, subject, data = payload2fields(txt)
                sender, recipient, subject, message = cleanFieldsEmails(sender, recipient, subject, data)
    else :
        sender, recipient, subject, message = "No emails!","","",""
    
    return sender, recipient, subject, message

    