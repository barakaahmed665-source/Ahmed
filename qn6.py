class Student:
    
    def __init__(self,student_ID,name,age,gender,programe,year_of_study,tuition_balance,registered,courses):
        
        
        self.student_ID =student_ID
        self.name =name
        self.age =age
        self.gender =gender
        self.programe =programe
        self.year_of_study =year_of_study

        #private tuition
        self.__tuition_balance =tuition_balance
        self.registered =registered
        self.courses =courses
        

    #Displaying  student's details
    def display_details(self):
        print("\n  Student details  ")
        print("Student ID :",self.student_ID)
        print("Name :",self.name)
        print("Age :",self.age)
        print("Gender :",self.gender)
        print("Program :",self.programe)
        print("Year of Study :",self.year_of_study)
        print("Tuition balance :",self.__tuition_balance)
        print("Registered :",self.registered)
        print("Course :",self.courses)
        
#Registering the courses
    def register_course(self,course):
        
        self.courses.append(course)
        print(course,"has been registered successfully")

    def pay_tuition(self,amount):
        if  amount <= self.__tuition_balance:
            self.__tuition_balance =self.__tuition_balance -amount
            print("Tuition Payment of ",amount,"has been made")
            print("New tuition balance is ",self.__tuition_balance)
        else:
            print("Tuition cannot be made")
            print("Tuition balance is less than the amount paid. Payment not made")

    def check_registration(self):
        if self.registered ==True:
            print("Student registered ")

        else:
            print("Unregistered")

    def get_tuition_balance(self):
        return self.__tuition_balance

    #Five students objects
student1 =Student("B100","Amule",23,"M","Library",2,2300.5,True,["Library ethics"," Principle of Managemnt"])
student2 =Student("B200","Akbar",23,"M","Business Studies",3,25500.50,True,["Accounting","Finance"])
student3 =Student("B300","Samuel",22,"M","Computer Science",2,12400.32,True,["Computing","Discrete Math"])
student4 =Student("B400","Kendito",22,"F","Social Work",3,12400.32,True,["Urban Development","Human Behaviors"])
student5 =Student("B500","Allice",22,"F","Social Work",2,12400.32,True,["Urban Development","Human Behaviors"])

#Displaying all details of students
print("STUDENT MANAGEMENT SYSTEM FOR KAMPALA UNIVERSITY")

student1.display_details()
student2.display_details()
student3.display_details()
student4.display_details()
student5.display_details()

#Adding courses

print("\n ADDING STUDENT COURSES")
print("\n Student 1")
student1.register_course("Computer application")
student1.register_course("Islamic banking")
print("\n Student 2")
student2.register_course("Prepositions")
student2.register_course("IT Ethics")

#Checking registration
print("\n CHECKING STUDENT REGISTRATION")
print("\n Student 3 and 4")
student3.check_registration()
student4.check_registration()

#Paying Tuition
print("\n Student5")
student5.pay_tuition(2560000)
print("\n Student 1")
student1.pay_tuition(2999.87)

#Getting Tuition balance
print("GETTING TUITION BALANCE")
print("\n Student 3")
student3.get_tuition_balance()
print("\n Student 5")
student5.get_tuition_balance()

#Data types
print("\n DATA TYPES")
print("\n  Student1 details  ")
print("Student ID :",type(student1.student_ID))
print("Name :",type(student1.name))
print("Age :",type(student1.age))
print("Gender :",type(student1.gender))
print("Program :",type(student1.programe))
print("Year of Study :",type(student1.year_of_study))
print("Tuition balance :",type(student1.get_tuition_balance))
print("Registered :",type(student1.registered))
print("Course :",type(student1.courses))



#Display all student 1 details
student1.display_details()



    



    
    