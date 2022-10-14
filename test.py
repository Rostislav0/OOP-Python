class Wallet:
    def __init__(self, currency, balance):
        if not isinstance(currency, str):
            raise TypeError('Неверный тип валюты')
        elif len(currency) != 3:
            raise NameError('Неверная длина названия валюты')
        elif currency != currency.upper():
            raise ValueError('Название должно состоять только из заглавных букв')
        self.currency = currency
        self.balance = balance

    def __eq__(self, other):
        if isinstance(other, Wallet):
            if other.currency != self.currency:
                raise ValueError('Нельзя сравнить разные валюты')
            return other.balance == self.balance
        raise TypeError(f'Wallet не поддерживает сравнение с {other}')

    def __add__(self, other):
        if isinstance(other, Wallet) and other.currency == self.currency:
            sum = self.balance + other.balance
            return Wallet(self.currency, sum)
        raise ValueError('Данная операция запрещена')

    def __sub__(self, other):
        if isinstance(other, Wallet) and other.currency == self.currency:
             dif = self.balance - other.balance
             return Wallet(self.currency, dif)
        raise ValueError('Данная операция запрещена')

wallet1 = Wallet('USD', 50)
wallet2 = Wallet('RUB', 100)
wallet3 = Wallet('RUB', 150)
# wallet4 = Wallet(12, 150)  # исключение TypeError('Неверный тип валюты')
# wallet5 = Wallet('qwerty', 150)  # исключение NameError('Неверная длина названия валюты')
# wallet6 = Wallet('abc', 150)  # исключение ValueError('Название должно состоять только из заглавных букв')
# print(wallet2 == wallet3)  # False
# print(wallet2 == 100)  # TypeError('Wallet не поддерживает сравнение с 100')
# print(wallet2 == wallet1)  # ValueError('Нельзя сравнить разные валюты')
wallet7 = wallet2 + wallet3
print(wallet7.currency, wallet7.balance)  # печатает 'RUB 250'
wallet2 + 45  # ValueError('Данная операция запрещена')