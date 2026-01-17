# class variables- share value among all instances of class
# It is created outside of constructor
# share data among all the objects from that class


class Student:
    class_year = 2026
    number = 0

    def __init__(self, name,age):
        self.name = name
        self.age = age
        Student.number +=1

    

student1= Student('Biraj', 43)
student2= Student('Bishal', 33)
student3= Student('Mohit', 41)
# student4= Student('Basanta', 32)

print(f"The graduating class of {Student.class_year} has {Student.number} student. ")
print('They are: ')
print(student1.name)
print(student2.name)
print(student3.name)
# print(student4.name)