class Person:
    name = 'Vlad'
    old = 3


name = 'Ivan'
setattr(Person, 'old', 2)
setattr(Person, 'height', 189)
print(Person.__dict__)


# del Person.height

delattr(Person, 'height')
print(Person.__dict__)

a = Person()



class Lion:
    def roar(self):
        print('Rrrrrrr!!!')


simba = Lion()
simba.roar()