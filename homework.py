import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.remainder = self.limit
        self.records = []

    def add_record(self, calc_class):
        self.records.append(calc_class)
        self.remainder -= calc_class.amount

    def get_today_stats(self):
        return self.limit - self.remainder


class Record:
    def __init__(self, amount, comment, date=dt.datetime.now()):
        self.amount = amount
        self.comment = comment
        self.date = date

    def __str__(self):
        return f'{self.amount}, {self.comment}, {self.date}'


class CashCalculator(Calculator):
    USD_RATE = 74.04
    EURO_RATE = 89.62

    def __init__(self, limit):
        super().__init__(limit)
        self.limit_rub = self.remainder
        self.limit_usd = round(self.remainder / self.USD_RATE, 2)
        self.limit_euro = round(self.remainder / self.EURO_RATE, 2)

    def get_today_cash_remained(self, currency='rub'):
        if currency == 'rub':
            currency_get = self.limit_rub
            currency_str = 'руб'
        elif currency == 'usd':
            currency_get = self.limit_usd
            currency_str = 'USD'
        elif currency == 'euro':
            currency_get = self.limit_euro
            currency_str = 'Euro'
        if self.remainder > 0:
            return f"На сегодня осталось {currency_get} {currency_str}"
        elif self.remainder == 0:
            return 'Денег нет, держись'
        elif self.remainder < 0:
            return f"Денег нет, держись: твой долг - {currency_get} {currency_str}"


class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)


cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(10, 'test'))
print(cash_calculator.remainder)
print(cash_calculator.get_today_cash_remained('rub'))

