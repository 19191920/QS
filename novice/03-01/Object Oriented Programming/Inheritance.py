class schoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''Tell my details.'''
        print('name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


class Teacher(schoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        schoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('salary: "{:d}"'.format(self.salary))

class student(schoolMember):
    '''Represents a student.'''
    def __init__(self, namr, age, marks):
        ShoolMember.__init__(self, name, age)
        self.marks = marks   
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

    '''Represents a student.'''
    def __init__(self, name, age, marks):
        schoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initializes Student: {})'.format(self.name))

    def tell(self):
        schoolMember.tell(self)
        print('marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print()

members = [t, s]
for member in members:

    member.tell()
