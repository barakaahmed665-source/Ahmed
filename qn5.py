class Student:
    
    def __init__(self,student_ID,name,age,tuition_balance,registered,courses):
        
        
        self.student_ID =student_ID
        self.name =name
        self.age =age
            
            #private tuition
        self.__tuition_balance =tuition_balance
        self.registered =registered
        self.courses =courses

    def display_details(self):
        print("\nStudent ")
        print("Student ID :",self.student_ID)
        print("Name :",self.name)
        print("Age :",self.age)
        print("Tuition balance :",self.__tuition_balance)
        print("Registered :",self.registered)
        print("Course :",self.courses)

    def get_tuition_balance(self):
        return self.__tuition_balance

    def pay_tuition(self,amount):
        if self.__tuition_balance <= amount:
            self.__tuition_balance =self.__tuition_balance -amount
            print("Payment of ",amount,"has been made")
            print("New tuition balance is ",self.__tuition_balance)
        else:
            print("Tuition balance is less than the amount paid.!")

student1 = Student("B100","Amule",23,50000,True,["Information Systems","Computing"])

#Displaying student details
student1.display_details()

#Get tuition balance
student1.get_tuition_balance()

#getting tuition balance
student1.pay_tuition(50000)

#Displaying the tuition details after payment
print("Tuition balance after payment is ",student1.get_tuition_balance())
