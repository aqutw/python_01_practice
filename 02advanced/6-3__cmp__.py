class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return '<%s: %s>' % (self.name, self.score)
    __repr__ = __str__

    def __cmp__(self, other):
        if self.name < other.name:
            return -1
        elif self.name > other.name:
            return 1
        else:
            return 0

L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 77)]
print sorted(L)

print '----do Task---'
class Student2(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '<%s: %s>' % (self.name, self.score)

    __repr__ = __str__

    def __cmp__(self, s):
        if self.score == s.score:
            return cmp(self.name, s.name)
        return -cmp(self.score, s.score)

L = [Student2('Tim', 99), Student2('Bob', 88), Student2('Alice', 99)]
print sorted(L)
