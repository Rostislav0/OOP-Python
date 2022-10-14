class Person:
    def breathe(self):
        print('Человек дышит')

    def sleep(self):
        print('Человек спит')

    def combo(self):
        self.breathe()
        if hasattr(self, 'walk'):
            self.walk()
        self.sleep()

class Doctor(Person):

    def sleep(self):
        print('Доктор спит')

    def breathe(self):
        print('Доктор дышит')

    def walk(self):
        print('Доктор идёт')

p = Person()
p.combo()
d = Doctor()
d.combo()
