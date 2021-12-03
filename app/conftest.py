from config.config import Config

import pytest
import csv
import os
import codecs


@pytest.fixture
def create_csv_birthday():
    birthday = [
        ['12.01', '-A'],
        ['01.02', 'A'],
        ['02.02', 'B'],
        ['03.02', 'C'],
        ['04.02', 'D'],
        ['05.02', 'F'],
        ['06.02', 'G'],
    ]
    with open (Config.NAME_FILE_LIST_BIRTDAY, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(birthday)
    yield birthday
    os.remove(Config.NAME_FILE_LIST_BIRTDAY)

@pytest.fixture
def read_csv():
    r = list()
    with codecs.open(
        Config.NAME_FILE_LIST_BIRTDAY, encoding='utf-8'
    ) as f:
        _rec_birthday = csv.reader(f)
        for i in _rec_birthday:
            r.append(i)
    yield r
