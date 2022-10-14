class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property  # ЭТО ГЕТТЕР
    def old(self):
        return self.__old

    @old.setter  # ЭТО СЕТТЕР
    def old(self, old):
        self.__old = old

    @old.deleter  # А ЭТО ДЕЛИТЕР
    def old(self):
        del self.__old


p = Person('Сергей', 20)  # создаем экземпляр

print(p.old)  # получаем old

p.old = '222'  # устанавливаем old

del p.old  # удаляем old