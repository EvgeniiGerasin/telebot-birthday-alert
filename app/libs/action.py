from config.config import Config

import csv
import codecs
from datetime import datetime


class Helper:

    @staticmethod
    def to_format(date):
        """Приводит строку вида %d.%m.%Y к типу datetime

        Args:
            date (str): дата вида %d.%m.%Y

        Returns:
            datetime type
        """
        return datetime.strptime(date, "%d.%m.%Y")

    @staticmethod
    def read_from_csv(name_file: str):
        """Читает файл *.csv

        Args:
            name_file (str): имя файла для чтения

        Returns:
            csv type
        """
        r = list()
        with codecs.open(r"app\db\\" + name_file, encoding='utf-8') as f:
            # Данные вида ['дата', 'Имя']
            _rec_birthday = csv.reader(f)
            for i in _rec_birthday:
                r.append(i)
        return r


class DataBase:

    def __init__(self) -> None:

        _date_today = datetime.now().date()
        _date_today = f"{_date_today.day}.{_date_today.month}.{_date_today.year}"
        self._date_today = Helper.to_format(_date_today)
        self._rec_birthday = Helper.read_from_csv(
            Config.NAME_FILE_LIST_BIRTDAY
        )
        self._status_img = ''

    def get_all_birthday(self):
        """Получение словаря с данными о дате ДР всех сотрудников.

        Returns:
            (dict): key<name> : value<date>
        """
        birthdays = dict()
        for date, name in self._rec_birthday:
            date_birthday = Helper.to_format(
                date + '.' + str(self._date_today.year)
            )
            self._set_status_birthday(date_birthday=date_birthday)
            birthdays[name] = self._status_img + ' ' + date
        return birthdays

    def get_current_month_birthday(self):
        """Получение словаря с данными о дате ДР 
        сотрудников в текущем месяце.

        Returns:
            (dict): key<name> : value<date>
        """
        birthdays = dict()
        for date, name in self._rec_birthday:
            date_birthday = Helper.to_format(
                date + '.' + str(self._date_today.year)
            )
            if self._date_today.month == date_birthday.month:
                self._set_status_birthday(date_birthday=date_birthday)
                birthdays[name] = self._status_img + ' ' + date
        return birthdays

    def _set_status_birthday(self, date_birthday):
        """Установить эмодзи рядом с датой ДР

        🟢 - прошло |
        🟣 - еще будет |
        ⚡ - будет через 3/2/1 день |
        🎈 - сегодня 

        Args:
            date_birthday (datetime): дата ДР сотрудника
        """
        date_difference = str(self._date_today - date_birthday)
        # если есть day в date_difference
        if 'day' in date_difference:
            # 3 дня до ДР
            if date_difference[:6] in ('-1 day', '-2 day', '-3 day'):
                self._status_img = '⚡'
            # больше 3 дней до ДР
            elif '-' in date_difference:
                self._status_img = '🟣'
            # ДР уже был
            else:
                self._status_img = '🟢'
        # Если нет day в date_difference значит это день ДР
        else:
            self._status_img = '🎈'
