a1 = int(input())
a2 = int(input())
a3 = int(input())

class Third:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def equal(self):
        if self.a == self.b:
            print(3)
        elif self.a == self.c:
            print(2)
        else:
            print(1)


test = Third(a1,a2,a3)
test.equal()