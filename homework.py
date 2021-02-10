import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.remainder = self.limit

        # Список записей.
        self.records = []

        # Работа с датой.
        self.date_now = dt.datetime.now().date()

    def add_record(self, calc_class):
        self.records.append(calc_class)

    def get_today_stats(self):
        return sum([spent.amount for spent in self.records
                    if spent.date == self.date_now])

    def get_week_stats(self):
        return sum([spent.amount for spent in self.records
                    if self.date_now >= spent.date >= self.date_now -
                    dt.timedelta(days=7)])


class Record:

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        self.date = date
        if self.date:
            if type(self.date) == str:
                self.date = dt.datetime.strptime(self.date, '%d.%m.%Y').date()
        else:
            self.date = dt.datetime.now().date()

    def __str__(self):
        return f'{self.amount}, {self.comment}, {self.date}'


class CashCalculator(Calculator):
    # Курс валют.
    USD_RATE = 74.04
    EURO_RATE = 89.62
    RUB_RATE = 1

    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency='rub'):

        # Конвертация валют.
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

        limit_rate = abs(round((self.limit - self.get_today_stats())
                               / exchange[currency]['rate'], 2))
        limit_type = exchange[currency]['type']

        costs = self.get_today_stats()

        if self.limit > costs > 0:
            return f'На сегодня осталось {limit_rate} {limit_type}'
        elif self.limit == costs:
            return 'Денег нет, держись'
        elif self.limit < costs:
            return f'Денег нет, держись: твой долг - {limit_rate} {limit_type}'


class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):

        eaten = self.get_today_stats()
        remainder = self.limit - eaten

        if self.limit > eaten:
            return (f'Сегодня можно съесть что-нибудь ещё, но с общей '
                    f'калорийностью не более {remainder} кКал')
        elif self.limit <= eaten:
            return f'Хватит есть!'


if __name__ == '__main__':
    cash_calculator = CashCalculator(1000)
    cash_calculator.add_record(Record(amount=145, comment='кофе'))
    cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
    cash_calculator.add_record(Record(amount=3000,
                                      comment='бар в Танин др',
                                      date='08.11.2019'))

    print(cash_calculator.get_today_cash_remained('rub'))
