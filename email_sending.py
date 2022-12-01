import datetime

import config
from storage import save_to_json_file

__all__ = [
    'send_email_smtp'
]


def send_email_smtp(to: str, subject: str, html_content: str) -> None:
    save_to_json_file(EmailLetter(to, subject, html_content), config.EMAILS_JSON_DUMP_FILE)


class EmailLetter:
    def __init__(self, to: str, subject: str, html_content: str):
        self.to: str = to
        self.subject: str = subject
        self.html_content: str = html_content
        self.created: str = datetime.datetime.now().strftime('%a %m, %H:%M')
