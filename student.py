from person import Person
class Student(Person):
    def __init__(self, school ,first, last, dob, phonenumber, address, international=False):
        super().__init__(first, last, dob, phonenumber, address)
        self.international = international
        self.enrolled = list()
        self._school = school

    def enroll(self, course):
        _course = self._school.getCoursebyname(course)
        _course.students.append(self)
        self.enrolled.append(_course)
        self._school.enrolls.append((self, _course))

    def isPartTime(self):
        return len(self.enrolled) <=2

    def isOnProbation(self):
        return False

