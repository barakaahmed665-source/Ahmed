class Student:
    def __init__(self,student_ID,name,age,programe,tuition_balance =0):
        self.student_ID =student_ID
        self.name =name
        self.age =age
        self.programe =programe
        self.tuition_balance =tuition_balance
#Students Objects
student1=Student("B100","Amule",23,"Business",2300.5)
student2 =Student("B200","Akbar",23,"Business Statistics",25500.50)
student3 =Student("B300","Samuel",22,"Computer Science",12400.32)


#Displaying the results
print("\nStudent 1")
print("Student ID :",student1.student_ID)
print("Name :",student1.name)
print("Age :",student1.age)
print("Programme :",student1.programe)
print("Tuition balance :",student1.tuition_balance)

#Student2 Details
print("\nStudent 2")
print("Student ID :",student2.student_ID)
print("Name :",student2.name)
print("Age :",student2.age)
print("Programme :",student2.programe)
print("Tuition balance :",student2.tuition_balance)

#Student 3 Details
print("\n Student 3")
print("Student ID :",student3.student_ID)
print("Name :",student3.name)
print("Age :",student3.age)
print("Programme :",student3.programe)
print("Tuition balance :",student3.tuition_balance)