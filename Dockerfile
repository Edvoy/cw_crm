FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . ./
EXPOSE 8000
CMD ["python", "./crm/manage.py", "runserver", "0.0.0.0:8000", "--settings=crm.settings"] && ["python", "./crm/manage.py", "crontab add"]