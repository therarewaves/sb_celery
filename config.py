import glob
import os

BASE_URL = 'http://127.0.0.1:5000/'
REDIS_BROKER = REDIS_BACKEND = '127.0.0.1:6379'
TEST_USER_EMAIL = 'test@test.test'
CREATING_REPORT_DELAY = 3  # seconds
MEDIA_PATH = os.path.join(os.getcwd(), 'media')

EMAILS_JSON_DUMP_FILE = os.path.join(MEDIA_PATH, 'emails.json')
REPORTS_JSON_DUMP_FILE = os.path.join(MEDIA_PATH, 'reports.json')


def clean_media() -> None:
    if os.path.isdir(MEDIA_PATH):
        for f in glob.glob(f'{MEDIA_PATH}/*'):
            os.remove(f)
    else:
        os.mkdir(MEDIA_PATH)


clean_media()
