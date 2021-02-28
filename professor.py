from person import Person

class Professor(Person):

    def __init__(self, school, first, last, dob, phonenumber, address, salary):
        super().__init__(first, last, dob, phonenumber, address)
        self.salary = salary
        self.courses = []
        self.bonus = 0
        self.ID = None
        self._school = school
    def isGoodperform(self):
        return len(self.courses) > 3
    def addBonus(self):
        if self.isGoodperform():
            self.bonus = 20000
    def addCourse(self, course):
        self.courses.append(course)
    # def isTeaching(self, course):
    #     return True if course in self.courses else False
    def setGrade(self,course, student, grade):
        course.setGrade(self, student, grade)

