import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record_class):
        self.records.append(record_class)

    def get_today_stats(self):
        date_now = dt.datetime.now().date()
        return sum(record.amount for record in self.records
                   if record.date == date_now)

    def get_week_stats(self):
        date_now = dt.datetime.now().date()
        weekly_timedelta = date_now - dt.timedelta(days=7)
        return sum(record.amount for record in self.records
                   if weekly_timedelta < record.date <= date_now)

    def today_remained(self):
        return self.limit - self.get_today_stats()


class Record:
    DATE_FORMAT = '%d.%m.%Y'

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment

        if date is not None:
            self.date = dt.datetime.strptime(date, self.DATE_FORMAT).date()
        else:
            self.date = dt.date.today()

    def __str__(self):
        return f'{self.amount}, {self.comment}, {self.date}'


class CashCalculator(Calculator):
    USD_RATE = 74.04
    EURO_RATE = 89.62
    RUB_RATE = 1

    def get_today_cash_remained(self, currency):
        exchange = {
            'rub': (self.RUB_RATE, 'руб'),
            'usd': (self.USD_RATE, 'USD'),
            'eur': (self.EURO_RATE, 'Euro'),
        }

        if currency not in exchange:
            return 'Валюта не поддерживается'

        remainder = self.today_remained()

        if remainder == 0:
            return 'Денег нет, держись'

        rate, limit_type = exchange[currency]
        limit_rate = round(remainder / rate, 2)

        if limit_rate < 0:
            abs_limit_rate = abs(limit_rate)
            return (f'Денег нет, держись: твой долг - {abs_limit_rate} '
                    f'{limit_type}')
        return f'На сегодня осталось {limit_rate} {limit_type}'


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        remainder = self.today_remained()

        if remainder > 0:
            return ('Сегодня можно съесть что-нибудь ещё, но с общей '
                    f'калорийностью не более {remainder} кКал')
        return 'Хватит есть!'
