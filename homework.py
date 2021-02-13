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
        return sum(n.amount for n in self.records if date_now
                   >= n.date > weekly_timedelta)

    def today_remained(self):
        return self.limit - self.get_today_stats()


class Record:

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment

        if date is not None:
            if type(date) == str:
                date = dt.datetime.strptime(date, '%d.%m.%Y').date()
            else:
                date = dt.datetime.date(date)
        else:
            date = dt.datetime.now().date()
        self.date = date

    def __str__(self):
        return f'{self.amount}, {self.comment}, {self.date}'


class CashCalculator(Calculator):
    USD_RATE = 74.04
    EURO_RATE = 89.62
    RUB_RATE = 1

    def get_today_cash_remained(self, currency='rub'):

        exchange = {
            'rub': {
                'rate': self.RUB_RATE,
                'type': 'руб'
            },
            'usd': {
                'rate': self.USD_RATE,
                'type': 'USD'
            },
            'eur': {
                'rate': self.EURO_RATE,
                'type': 'Euro'
            },
        }

        limit_rate = round(self.today_remained()
                           / exchange[currency]['rate'], 2)
        limit_type = exchange[currency]['type']

        if limit_rate == 0:
            return 'Денег нет, держись'
        elif limit_rate > 0:
            return f'На сегодня осталось {limit_rate} {limit_type}'
        else:
            return (f'Денег нет, держись: твой долг - {abs(limit_rate)} '
                    f'{limit_type}')


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        remainder = self.today_remained()

        if remainder > 0:
            return ('Сегодня можно съесть что-нибудь ещё, но с общей '
                    f'калорийностью не более {remainder} кКал')
        else:
            return 'Хватит есть!'


if __name__ == '__main__':
    cash_calculator = CashCalculator(1000)
    cash_calculator.add_record(Record(amount=145, comment='кофе'))
    cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
    cash_calculator.add_record(Record(amount=3000,
                                      comment='бар в Танин др',
                                      date='08.11.2019'))

    print(cash_calculator.get_today_cash_remained('rub'))
