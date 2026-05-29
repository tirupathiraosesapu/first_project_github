class Counter:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.num > 5:
            raise StopIteration

        value = self.num
        self.num += 1
        return value


value = Counter()

# item = iter(value)

# print(item.__next__())
# print(item.__next__())
print(value.__next__())
print(value.__next__())
print(value.__next__())
print(value.__next__())
print(value.__next__())
print(next(value))
