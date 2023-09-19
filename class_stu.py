class Course:

    def __init__(self, course_id, course_name, course_class,course_mark):
        self.course_id = course_id
        self.course_name = course_name
        self.course_class = course_class
        self.course_mark = course_mark

    def get_course_details(self):
        print(str(self.course_id) + "\t|\t" + self.course_name + "\t|\t" + self.course_class +str(self.course_mark) )


class Student:

    def __init__(self, student_id, student_name, student_age ,student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class
        self.student_age = student_age
        self.courses_list = []

    def enroll_course(self, course):
        if self.student_class == course.course_class:
            for i in self.courses_list:
                if course.course_id == i.course_id:
                    print("||Course Already Enrolled||")
                    return
            self.courses_list.append(course)
            print("||Course Enrolled Successfully||")
        else:
            print("||Invalid Course Class||")

    def get_student_details(self):
        print(str(self.student_id) + "\t|\t" + self.student_name + "\t|\t"+ str(self.student_age)+"\t|\t" + self.student_class)
        if len(self.courses_list) == 0:
            print("||Courses List Empty||")
            return
        print("Courses List >>> ")
        for course in self.courses_list:
            print(course.course_name+" | "+course.course_mark)
student_list = []
courses_list = []

def get_courses_list(courses):
    print("ID\t|\tName\t|\tClass\t|\t Mark")
    for course in courses:
        course.get_course_details()

def get_students_details(students):

    print("ID\t|\tName\t|\tClass")
    for student in students:
        print(student.get_student_details())


def find_student(student_id,students):
    index = 0
    for student in students:
        if student.student_id == student_id:
            return index
        index += 1
    return -1

def find_averagecourse(course_id,courses):
  average=0
  for course in courses:
      if course.course_id == course_id:
          average+=course.course_mark
          average/=3
          return average
def find_course(course_id,courses):
    index = 0
    for course in courses:
        if course.course_id == course_id:
            return index
        index += 1
    return -1

while True:
    selection = int(input("#Select Choice Please\n1.Add New Student\n2.Remove Student"
                          "\n3.Edit Student\n4.Display All Students\n5.Create New Course"
                          "\n6.Add Course To Student"
                          "\n7.Get Student average"
                          "\n8.Exit"
                          "\n*Enter Your Choice:"))

    if selection == 1:
        student_name = input("*Enter Student Name:")
        while True:
            student_class =  input("*Select Student Class (A-B-C):")
            if student_class in ['A','B','C']:
                break
        student_id = len(student_list) + 1
        student_age = input("*Enter Student Age:")
        student = Student(student_id,student_name,student_age,student_class)
        student_list.append(student)
        print("||Student Created Successfully||")
    elif selection == 2:
        get_students_details(student_list)
        student_id = int(input("*Enter Student ID:"))
        student_index = find_student(student_id,student_list)
        if student_index == -1 :
            print("||Student Not Exist||")
        else:
            student_list.pop(student_index)
            print("||Student Removed Successfully||")
            get_students_details(student_list)

    elif selection == 3:
        get_students_details(student_list)
        student_id = int(input("*Enter Student ID:"))
        student_index = find_student(student_id, student_list)
        if student_index == -1:
            print("||Student Not Exist||")
        else:
            student_name = input("*Enter Student Name:")
            while True:
                student_class = input("*Select Student Class (A-B-C):")
                if student_class in ['A', 'B', 'C']:
                    break
            student_list[student_index].student_name = student_name
            student_list[student_index].student_class = student_class
            print("||Student Details Updated Successfully||")
    elif selection == 4:
        get_students_details(student_list)
    elif selection == 5:
        course_name = input("*Enter Course Name:")
        while True:
            course_class = input("*Select Course Class (A-B-C):")
            if course_class in ('A','B','C'):
                break
        course_mark = input("*Enter Course Mark:")
        course_id = len(courses_list) + 1
        course = Course(course_id,course_name,course_class, course_mark)
        courses_list.append(course)
        print("||Course Created Successfully||")
    elif selection == 6:
        get_courses_list(courses_list)
        student_id = int(input("*Enter Student ID:"))
        student_index = find_student(student_id,student_list)
        if student_index == -1:
            print("||Student Not Exist||")
        else:
            course_id = int(input("*Enter Course ID:"))
            course_index = find_course(course_id,courses_list)
            if course_index == -1:
                print("||Course Not Exist||")
            else:
                student_list[student_index].enroll_course(courses_list[course_index])
    elif selection == 7:
         student_id = int(input("*Enter Student ID:"))
         student_index = find_student(student_id, student_list)
         if student_index == -1:
             print("||Student Not Exist||")
         else:
             course_id = int(input("*Enter Course ID:"))
             course_index = find_course(course_id, courses_list)
             if course_index == -1:
                 print("||Course Not Exist||")
             else:
               average_std=str(find_averagecourse(course_id, courses_list))
               print(average_std)

    else:
        exit()
