class Student:
    pass

student =Student()

student.student_ID ="B100"
student.name = "Faida"
student.age = 16
student.Tuition_balance =float(1000.50)
student.Registered =False
student.Courses =["Object Oriented programming"]

#Printing the values

print("Student ID :",student.student_ID)
print("Name :",student.name)
print("Age :",student.age)
print("Tuition balance :",student.Tuition_balance)
print("Registered :",student.Registered)
print("Courses:",student.Courses)

#Printing the data types
print("\n Data Types")
print(type(student.student_ID))
print(type(student.name))
print(type(student.age))
print(type(student.Tuition_balance))
print(type(student.Registered))
print(type(student.Courses))

#Adding three courses to the list
student.Courses.append("Statistics")
student.Courses.append("Computer Application")
student.Courses.append("Accounts")

#Printing the courses
print("\n Courses")
print(student.Courses)