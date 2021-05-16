from emails.views import syncMails

def my_cron_job():
    syncMails()