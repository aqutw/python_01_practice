############# 1
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

s = Student('Bob', 59)
s.score = 60

############### 2

class Student2(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    def get_score(self):
        return self.__score
    def set_score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score


############### 3
class Student3(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
 
s = Student3('Bob', 59)
s.score = 60
print s.score
try:
    s.score = 1000 #<--- now throw ValueError
except:
    print 'ValueError'

############ Task
print '----do Task---'
class Student4(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
    @property
    def grade(self): # grade will be readonly
        if self.score>=80: return 'A'
        elif self.score>=60: return 'B'
        else: return 'C'

s = Student4('Bob', 59)
print s.grade
s.score = 60
print s.grade
s.score = 99
print s.grade
