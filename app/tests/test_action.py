from config.config import Config
from libs.action import Helper, DataBase

from datetime import datetime
import pytest
import codecs
import csv


STATUS_AND_DATE = {
    'date_future': ('11.01.2020', '🟣'),
    'date_three': ('01.02.2020', '⚡'),
    'date_two': ('02.02.2020', '⚡'),
    'date_one': ('03.02.2020', '⚡'),
    'date_birthday': ('04.02.2020', '🎈'),
    'date_past': ('12.02.2020', '🟢'),
}


class TestAction:

    def test_to_format(self):
        str_to_converting = '21.11.2121'
        want = datetime.strptime(str_to_converting, '%d.%m.%Y')
        got = Helper.to_format(str_to_converting)
        assert want == got, f'want "{want}" != got "{got}"'

    @pytest.mark.parametrize(
        'date',
        {
            'date_past',
            'date_three',
            'date_two',
            'date_one',
            'date_birthday',
            'date_future',
        }
    )
    def test_set_status_birthday(self, date):
        date_birthday = datetime.strptime('04.02.2020', '%d.%m.%Y')
        db = DataBase()
        db._date_today = datetime.strptime(
            STATUS_AND_DATE[date][0],
            '%d.%m.%Y'
        )
        want = STATUS_AND_DATE[date][1]
        db._set_status_birthday(date_birthday=date_birthday)
        got = db._status_img
        assert want == db._status_img, f'want "{want}" != got "{got}"'

    def test_get_all_birthday(self, create_csv_birthday, read_csv):
        data_now = datetime.strptime('02.01.2020', '%d.%m.%Y')
        db = DataBase()
        db._date_today = data_now
        r = list()
        with codecs.open(
            Config.NAME_FILE_LIST_BIRTDAY, encoding='utf-8'
        ) as f:
            _rec_birthday = csv.reader(f)
            for i in _rec_birthday:
                r.append(i)
        db._rec_birthday = read_csv
        want = {
            'A': '🟢 01.01',
            'B': '🎈 02.01',
            'C': '⚡ 03.01',
            'D': '⚡ 04.01',
            'F': '⚡ 05.01',
            'G': '🟣 06.01'
        }
        got = db.get_all_birthday()
        assert want == got, f'want "{want}" != got "{got}"'

    def test_get_all_birthday(self, create_csv_birthday, read_csv):
        data_now = datetime.strptime('02.02.2020', '%d.%m.%Y')
        db = DataBase()
        db._date_today = data_now
        r = list()
        with codecs.open(
            Config.NAME_FILE_LIST_BIRTDAY, encoding='utf-8'
        ) as f:
            _rec_birthday = csv.reader(f)
            for i in _rec_birthday:
                r.append(i)
        db._rec_birthday = read_csv
        want = {
            '-A': '🟢 12.01',
            'A': '🟢 01.02',
            'B': '🎈 02.02',
            'C': '⚡ 03.02',
            'D': '⚡ 04.02',
            'F': '⚡ 05.02',
            'G': '🟣 06.02'
        }
        got = db.get_all_birthday()
        assert want == got, f'want "{want}" != got "{got}"'

    def test_get_current_month_birthday(self, create_csv_birthday, read_csv):
        data_now = datetime.strptime('02.02.2020', '%d.%m.%Y')
        db = DataBase()
        db._date_today = data_now
        r = list()
        with codecs.open(
            Config.NAME_FILE_LIST_BIRTDAY, encoding='utf-8'
        ) as f:
            _rec_birthday = csv.reader(f)
            for i in _rec_birthday:
                r.append(i)
        db._rec_birthday = read_csv
        want = {
            'A': '🟢 01.02',
            'B': '🎈 02.02',
            'C': '⚡ 03.02',
            'D': '⚡ 04.02',
            'F': '⚡ 05.02',
            'G': '🟣 06.02'
        }
        got = db.get_current_month_birthday()
        assert want == got, f'want "{want}" != got "{got}"'

    def test_to_format(self):

        date = "22.12.2020"
        datetime_date = Helper().to_format(date)
        want = "<class 'datetime.datetime'>"
        got = str(type(datetime_date))
        assert want == got, f'want "{want}" != got "{got}"'
