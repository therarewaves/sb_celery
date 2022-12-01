### Task description
There is a task when we have to request some reports and send them to the user's email.
The report files can be massive, 
so instead of direct sending we have to save the report files to the hard drive, 
and send to the user just a link to a page, when the report can be downloaded.
Apart from that we should use Celery and Redis.

### Usage
1. Click "Send me a report"
2. Wait, clicking "reload" on the same page
3. You'll get a mock email with the link to the report
4. Click the link "download it here" - you will be redirected to a new page
5. Download the file and go back

### Solution description

This app has two pages:
1. request a new report, and view the user's email box
2. download the report by the link from email

You are a test user with a frozen email: "test@test.test" (can be changed in config.py).
On the first page you can request a report, which should be sent to your email. 
Instead of using smtp-sending the app save all the emails to a json-file 'emails.json' 
and then read all of them to the user's email inbox right on the first page.

When you click "Send me a report" the app creates a Celery task 
("request_report_and_send_to_email()"), 
which generates a csv file with a random name 
(and current time in the name) and random data inside. 
Saves the information about the report to the "reports.json" file 
(as a temporary data storage, because we don't use a database in this solution),
and sends an email with the link to the user.

### How to run

#### Run Redis

```
docker run -p 6379:6379 --name some-redis -d redis
```

#### Run Celery worker

```
celery -A tasks.celery worker --loglevel=info -E
```

#### Run flower (if needed)

```
celery -A tasks.celery flower --port=5555
```