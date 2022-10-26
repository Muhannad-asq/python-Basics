


class Student:
    def __init__(self,Name):
        print(f" welcome {Name} ")
        self.marks = []


    def add_mark (self,mark):
        self.marks.append(mark)



    def get_avg(self) :
        avg = sum(self.marks)/len(self.marks)
        print(avg)

Name = input(" Enter your name : ")
s1 = Student (Name)
s1.add_mark(60)
s1.add_mark(50)
s1.add_mark(80)
s1.add_mark(20)


s1.get_avg()


