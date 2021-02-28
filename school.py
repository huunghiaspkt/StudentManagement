from student import Student
from professor import  Professor
from course import  Course

class School():
    def __init__(self):

        self.courses = list()

        self.students   = list()

        self.professors = list()

        self.enrolls = list()


    def openCourse(self, name, min, max):
        _course = Course(name, min, max)
        self.courses.append(_course)

    def addProfess2Course(self, professor, course):
        _professor = self.getProfessorbyName(professor)
        _course = self.getCoursebyname(course)
        _course.professors.append(_professor)

    def addStudent(self, first, last, dob, phonenumber, address, international=False):
        _student = Student(self,first, last, dob, phonenumber, address, international)
        self.students.append(_student)
        return _student

    def addProfessor(self,first, last, dob, phonenumber, address, salary):
        _professor = Professor(self,first, last, dob, phonenumber, address, salary)
        self.professors.append(_professor)
        return _professor

    def getCourseInfo(self):
        for course in self.courses:
            course.printInfo()
    def getStudentByName(self, name):
        pass

    def getCoursebyname(self, coursename):
        for course in self.courses:
            if course.name == coursename:
                return course

    def getProfessorbyName(self, professor):
        for _professor in self.professors:
            if _professor.lastName == professor:
                return _professor

if __name__ == '__main__':
    WE =School()
    WE.openCourse('SofwareArchi', 10, 100)
    WE.openCourse('Linux', 10,50)
    WE.openCourse('AI', 2, 20)

    sJack = WE.addStudent('Nguyen', 'Jack', '11,11,1985', '0775207480', ['HCM','BinhChanh','NguyenVanLinh'])
    sTech = WE.addStudent('Nguyen', 'Tech', '11,11,1985', '0775207480', ['HCM', 'BinhChanh', 'NguyenVanLinh'])
    sJamp = WE.addStudent('Nguyen', 'Jamp', '11,11,1985', '0775207480', ['HCM', 'BinhChanh', 'NguyenVanLinh'])
    sJuddy = WE.addStudent('Nguyen', 'Juddy', '11,11,1985', '0775207480', ['HCM', 'BinhChanh', 'NguyenVanLinh'])

    tMJ = WE.addProfessor('Nguyen', 'MJ', '11,11,1985', '0775207480', ['HCM', 'BinhChanh', 'NguyenVanLinh'], 9000)

    WE.addProfess2Course('MJ', "SofwareArchi")

    sJack.enroll("SofwareArchi")
    sTech.enroll("SofwareArchi")
    sJamp.enroll("SofwareArchi")

    for course in WE.courses:
        _course = course.name
    mycourse = WE.getCoursebyname("SofwareArchi")
    for students in mycourse.students:
        student = students.lastName
        print(f'SofwareArchi: {student}')
    for tech in mycourse.professors:
        profess = tech.lastName
        print(f'SofwareArchi: {profess}')


