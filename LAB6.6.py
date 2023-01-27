class student:
    def __init__(self,input):
        self.id = input
        print('id:', self.id)
    def student_class(self,input):
        self.student_class = input
        print('class:', self.student_class)
    def student_name(self,input):
        self.student_name = input
        print('name:',self.student_name)
a = student(12)
a.student_name("John")
a.student_class("9b")

