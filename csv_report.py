import csv
import datetime
import random
import string
from io import StringIO
from os.path import join
from typing import Generator, Optional

import config
from storage import save_to_json_file

__all__ = [
    'RandomCsvReport',
]


class RandomCsvReport:
    __id: int = 0

    def __init__(self, creator_email: str):
        self.id = self.generate_id()

        self.name: str = self.get_some_name()
        self.path: Optional[str] = None
        self.csv: StringIO = self.make_random_csv_report()
        self.created: datetime.datetime = datetime.datetime.now()
        self.creator_email: str = creator_email

    @staticmethod
    def get_some_name() -> str:
        return f'report_{RandomCsvReport._random_string(length=5).lower()}_' \
               f'{datetime.datetime.now().strftime("%Y.%d.%m_%H.%M.%S")}.csv'

    @classmethod
    def generate_id(cls) -> int:
        cls.__id += 1
        return cls.__id

    @staticmethod
    def _random_string(length: int = 10) -> str:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    @staticmethod
    def make_random_csv_report() -> StringIO:
        def _random_data(column_length: int) -> Generator:
            return ((RandomCsvReport._random_string() for _ in range(column_length))
                    for _ in range(random.randint(100, 1000)))

        def _random_header() -> list:
            return [f'Data {string.ascii_uppercase[i]}'
                    for i in range(0, random.randint(5, len(string.ascii_uppercase)))]

        header: list = _random_header()
        data: Generator = _random_data(len(header))

        csv_file = StringIO()
        writer = csv.writer(csv_file)
        writer.writerow(header)
        writer.writerows(data)

        return csv_file

    def save_to(self, path: str) -> None:
        full_path = join(path, self.name)
        with open(full_path, mode='w') as f:
            print(self.csv.getvalue(), file=f)
        self.path = full_path
        self.csv = None

        save_to_json_file(self, config.REPORTS_JSON_DUMP_FILE)
