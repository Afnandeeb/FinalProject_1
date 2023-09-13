class Course:

    def __init__(self, course_id, course_name, course_mark):
        self.course_id = course_id
        self.course_name = course_name
        self.course_mark = course_mark

    def get_course_details(self):
        print(str(self.course_id) + "\t|\t" + self.course_name + "\t|\t" + str(self.course_mark))