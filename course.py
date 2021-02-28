from professor import  Professor
from student import Student

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Course:
    __metaclass__ = Singleton
    def __init__(self, name, min, max):
        self.name = name
        self.minStudent = min
        self.maxStudent = max
        self.professors = list()
        self.students = list()

    def printInfo(self):
        print(f'Course Name {self.name}')

    def _isStudent(self, student):
        return isinstance(student, Student)

    def _isProfessor(self, professor):
        return isinstance(professor, Professor)

    def isFull(self):
        return len(self.students) >= self.maxStudent
    def isCanceled(self):
        return len(self.students) < self.minStudent
    def isActive(self):
        return not (self.isFull() & self.isCanceled()) & self.id
    def isInprofessors(self, professor):
        return True if professor in self.professors else False
    def isInStudents(self, student):
        return True if student in self.students else False
