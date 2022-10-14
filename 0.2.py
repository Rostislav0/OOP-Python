class Counter:
    def start_from(self, x=0):
        self.x = x
    def increment(self):
        self.x += 1
    def display(self):
        print('Текущее значение счетчика =', self.x)

    def reset(self):
        self.x = 0
c1 = Counter()
c1.start_from()
c1.increment()
c1.display()
c1.increment()
c1.display()
c1.start_from(3)
c1.display()
c1.reset()
c1.display()