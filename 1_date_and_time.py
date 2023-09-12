from datetime import datetime,timedelta
"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    today=datetime.now()
    yesterday=today - timedelta(days=1)
    one_mouth_ago=today - timedelta(days=30)
    print(f"{yesterday.strftime('%d-%m-%Y')}\n{today.strftime('%d-%m-%Y')}\n{one_mouth_ago.strftime('%d-%m-%Y')}")


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    str_date=datetime(2020, 1, 1, 12, 10, 3, 234567)
    return str_date

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
