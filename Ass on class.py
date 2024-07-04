# class BankAccount:
#     def __init__(self, acctName, acctNo, acctBalance):
#         self.acctName=acctName
#         self.acctNo=acctNo
#         self.acctBalance=acctBalance
#     def Deposit(self):
#         deposit= 100000
#         self.deposit= deposit+self.acctBalance
#         return self.deposit
#     def Withdraw(self):
#         withdraw=30000
#         self.withdraw=self.deposit-withdraw
#         return self.withdraw
#     def CheckBalance(self):
#         balance=self.withdraw
#         return balance

# bankAcct=BankAccount("Barakat", 12345678890, 10000000)
# bankAcct2=BankAccount("Bahirat", 2345678901, 300000)
# print(f"After depositing, the account balance is: {BankAccount.Deposit(bankAcct)}")
# print(f"After withdrawing, the account balance is: {BankAccount.Withdraw(bankAcct)}")
# print(f"After depositing and withdrawing, the current account balance is: {BankAccount.CheckBalance(bankAcct)}")




class Person():
    def __init__(self, name, age, height):
        self.name=name
        self.age=age
        self.height=height
    def General(self):
        print(f"This is {self.name},  {self.age}year old, with an height of {self.height}cm")

class Student(Person):
    # def students(self, level):
    #     self.level= level
    #     print(f"The student name is {self.name} {self.age}year old, with an height of {self.height}cm and in {self.level}level")
    #another formular
    def __init__(self, name, age, height, level):
        super().__init__(name, age, height)
        self.level= level
        print(f"The student name is {self.name} {self.age}year old, with an height of {self.height}cm and in {self.level}level")
        

# class Lecturer(Person):
#     def lecturers(self, course):
#         self.course=course
#         # print(f"The lecturer name is {self.name} {self.age}year old, with an height of {self.height}cm and in charge of {self.course} course")
#         print(f"The lecturer age is {self.age}year old, with an height of {self.height}cm and in charge of {self.course} course")

person1= Person("Ade", 31, 60)
person2= Student("Tomori Barakat", 25, 61, 500)
# person3=Lecturer("Prof Adeolu", 70, 57)

person1.General()
# person2.students(500)
# person3.lecturers("AGY508")


