'''
ref:https://www.youtube.com/watch?v=JeznW_7DlB0
'''
class Pat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print("I am {0}, age is {1}".format(self.name, self.name))
    def speak(self):
        print('Default speaking')

class Cat(Pat):
    def __init__(self, name, age, color):
        super().__init__(name, age) #inherit Pat's __init__ atts
        self.color = color
    def speak(self):
        print('Meow')
    def show(self):
        print("I am {0}, age is {1}, color is {2}".format(self.name, self.age, self.color))

class Dog(Pat):
    def speak(self):
        print('Bark')
p = Pat('A',19)
p.show()
p.speak()

c = Cat('C', 20,' Blue')
c.show()
c.speak()

print('-------------------------------------')


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade
class Course:
    def __init__(self, course_name, maxnum):
        self.course_name = course_name
        self.maxnum = maxnum
        self.students = []
    def add_student(self,student):
        if len(self.students) < self.maxnum:
            self.students.append(student)
            return True
        return False
    def get_avg_grade(self):
        v = 0
        for s in self.students:
            v += s.get_grade()
        return v/len(self.students)
s1 = Student('A', 19, 99)
s2 = Student('B', 20, 95)
s3 = Student('C', 30, 60)
c = Course('MATH',2)
c.add_student(s1)
c.add_student(s3)
print(c.students[0].grade)
print(c.course_name)
print(c.get_avg_grade())

print('-----------------------')


class Person:
    # class att
    num_of_people = 0 #constant att for class

    def __init__(self, name):
        self.name = name
        #Person.num_of_people += 1
        Person.add_person()

    @classmethod  #act on class itself
    def num_of_people_(cls):
        return cls.num_of_people
    
    @classmethod
    def add_person(cls):
        cls.num_of_people += 1
    
p1 = Person('TT')
print(p1.num_of_people)  # will check p1 this instance has att num_of_people , if no , check Person
p2 = Person('kk')
print(p2.num_of_people)
print(Person.num_of_people_())


print('----------------------')

class Math:
    @staticmethod #do somthing but don't change 
    def add(x,num):
        return x + num
print(Math.add(1,10))









