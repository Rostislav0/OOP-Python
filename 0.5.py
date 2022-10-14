class Zebra:
    def __init__(self):
        self.a = 0
    def which_stripe(self):
        if self.a % 2 == 0:
            print('Полоска белая')
        else:
            print('Полоска черная')
        self.a += 1


z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe() # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe() # печатает "Полоска белая"