class Student:
    
    def __init__(self,student_ID,name,age,course,tuition_balance,registered):
    
        self.student_ID =student_ID
        self.name =name
        self.age =age
        self.course =course
        self.tuition_balance =tuition_balance
        self.registered =registered
    
#Displaying Resulst
    def display_details(self):
        print("\nStudent ")
        
        print("Student ID :",self.student_ID)
        print("Name :",self.name)
        print("Age :",self.age)
        print("Course :",self.course)
        print("Tuition balance :",self.tuition_balance)
        print("Registered :",self.registered)
#Registering courses
    def register_course(self,course):
        
        self.course.append(course)
        print(course,"has been registered successfully")
#Displaying Tuition balance
    def pay_tuition(self,amount):
        self.tuition_balance =self.tuition_balance - amount
        print("Payment of",amount,"has been made")
#Checking Registration
    def check_registration(self):
        if self.registered ==True:
            print("Student registered ")

        else:
            print("Unregistered")

student1 =Student("B100","Amule",23,[],2300.5,False)
#Registering two courses
student1.register_course("OOp")
student1.register_course("Principles of Management")
student1.pay_tuition(25900)
student1.check_registration()
student1.display_details()

        

    