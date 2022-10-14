class Money:
    def __init__(self, dollars, cents):
        # self.__dollars = dollars
        # self.__cents = cents
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        # return self.__dollars
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, k):
        # self.__dollars = k
        if isinstance(k, int) and k >= 0:
            self.total_cents = (self.total_cents - (self.total_cents // 100 * 100)) + k * 100
        else:
            print('Error dollars')

    @property
    def cents(self):
        # return self.__cents
        return self.total_cents - self.total_cents // 100 * 100

    @cents.setter
    def cents(self, k):
        # self.__cents = k
        if isinstance(k, int) and 0 <= k <= 99:
            self.total_cents = self.total_cents - (self.total_cents - (self.total_cents // 100 * 100)) + k
        else:
            print('Error cents')

    def __str__(self):
        # return f"Ваше состояние составляет {self.__dollars} долларов {self.__cents} центов"
        return f"Ваше состояние составляет {self.total_cents//100} долларов {self.total_cents - self.total_cents//100*100} центов"

Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов