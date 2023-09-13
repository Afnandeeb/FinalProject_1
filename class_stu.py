class Course:

    def __init__(self, course_id, course_name, course_mark):
        self.course_id = course_id
        self.course_name = course_name
        self.course_mark = course_mark

    def get_course_details(self):
        print(str(self.course_id) + "\t|\t" + self.course_name + "\t|\t" + str(self.course_mark))
class Student:
  studentn_umber =0
  def __init__(self, student_id, student_name, student_age,student_number ):
         self.student_id = student_id
         self.student_name = student_name
         self.student_age = student_age
         self.student_number = student_number
         self.courses_list = []
         Student.studentn_umber+=1

  def enroll_course(self, course):
             if self.student_class == course:
                 for i in self.courses_list:
                     if course.course_id == i.course_id:
                         print("||Course Already Enrolled||")
                         return
                 self.courses_list.append(course)
                 print("||Course Enrolled Successfully||")
             else:
                 print("||Invalid Course Class||")
  def get_student_details(self):
        print(str(self.student_id)+"\t|\t"+self.student_name+"\t|\t"+self.student_class)
        if len(self.courses_list) == 0:
            print("||Courses List Empty||")
            return
        print("Courses List >>> ")
        for course in self.courses_list:
            print(course.course_name)