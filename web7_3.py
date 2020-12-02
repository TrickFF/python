class Iter:
    def __init__(self, start = 0):
        self.i = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= 5:
            self.i += 1
            return self.i - 1
        else:
            raise StopIteration


ob_1 = Iter(-2)
for i in ob_1:
    print(i)

ob_2 = Iter(2)
print()
for i in ob_2:
    print(i)

print()
for i in ob_2:
    print(i)
