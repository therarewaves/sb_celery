import os
import time

from celery import Celery

import config
from csv_report import RandomCsvReport
from email_sending import send_email_smtp

celery = Celery(
    __name__,
    broker=f'redis://{config.REDIS_BROKER}',
    backend=f'redis://{config.REDIS_BACKEND}'
)


@celery.task
def request_report_and_send_to_email(email: str) -> None:
    time.sleep(config.CREATING_REPORT_DELAY)

    report = RandomCsvReport(email)
    report.save_to(os.path.join(config.MEDIA_PATH))
    url = f'{config.BASE_URL}download_report/{report.id}/'
    link = f'<a href="{url}">here</a>'
    send_email_smtp(to=email, subject=f'Report {report.name}',
                    html_content=f'Your report is ready, now you can download it {link}')
