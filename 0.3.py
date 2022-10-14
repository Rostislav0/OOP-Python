class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, p):
        if type(p) == type(self):
            return ((self.x - p.x)**2 + (self.y - p.y)**2)**0.5
        else:
            print('Передана не точка')

p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
print(p1.__dict__)
p2.set_coordinates(4, 6)
print(p2.__dict__)
d = p1.get_distance(p2) # вернёт 5.0
p1.get_distance(10) # Распечатает "Передана не точка"