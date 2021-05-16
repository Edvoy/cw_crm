#todo:ImportError: attempted relative import with no known parent package
from .views import syncMails

def my_cron_job():
    syncMails()