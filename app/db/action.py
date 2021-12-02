import csv
import codecs
from datetime import datetime


class Helper:

    @staticmethod
    def to_sec(date):
        return date.timestamp()

    @staticmethod
    def to_format(date):
        return datetime.strptime(date, "%d.%m.%Y")

    @staticmethod
    def read_from_csv():
        r = list()
        with codecs.open('app\db\ДР СОКПО.csv', encoding='utf-8') as f:
            # Данные вида ['дата', 'Имя']
            records = csv.reader(f)
            for i in records:
                r.append(i)
        return r


class DataBase:

    @staticmethod
    def get_all_birthday():
        birthdays = dict()
        date_today = datetime.now().date()
        date_today = f"{date_today.day}.{date_today.month}.{date_today.year}"
        date_today = Helper.to_format(date_today)
        records = Helper.read_from_csv()
        status_img = ''
        for date, name in records:
            date_birthday = Helper.to_format(date + '.' + str(date_today.year))
            date_difference = str(date_today - date_birthday)
            # если есть day в date_difference
            if 'day' in date_difference:
                # 3 дня до ДР
                if date_difference[:6] in ('-1 day','-2 days','-3 days'):
                    status_img = '⚡'
                # больше 3 дней до ДР
                elif '-' in date_difference:
                    status_img = '🟣'
                # ДР уже был
                else:
                    status_img = '🟢'
            # Если нет day в date_difference значит это день ДР
            else:
                status_img = '🎈'
            birthdays[name] = status_img + ' ' + date
        return birthdays

    @staticmethod
    def get_current_month_birthday():
        birthdays = dict()
        date_today = datetime.now().date()
        date_today = f"{date_today.day}.{date_today.month}.{date_today.year}"
        date_today = Helper.to_format(date_today)
        records = Helper.read_from_csv()
        status_img = ''
        for date, name in records:
            date_birthday = Helper.to_format(date + '.' + str(date_today.year))
            if date_today.month == date_birthday.month:
                date_difference = str(date_today - date_birthday)
                # если есть day в date_difference
                if 'day' in date_difference:
                    # 3 дня до ДР
                    if date_difference[:6] in ('-1 day','-2 days','-3 days'):
                        status_img = '⚡'
                    # больше 3 дней до ДР
                    elif '-' in date_difference:
                        status_img = '🟣'
                    # ДР уже был
                    else:
                        status_img = '🟢'
                # Если нет day в date_difference значит это день ДР
                else:
                    status_img = '🎈'
                birthdays[name] = status_img + ' ' + date
        return birthdays
