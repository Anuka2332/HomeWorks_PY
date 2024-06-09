#დეკორატორი.--ერთმანეთის ქვემოთ მყოფ ფუნქციის @სახელი-თ გამოძახება, რომ ერთის გამოძახებითმეორეც გამოიძახოს და არგუმენტად გადაეცეს 1---
# def decor1(func):
#     def inner():
#         x = func()
#         return x * 4
#     return inner
# def decor2(func):
#     def inner():
#         x = func()
#         return x -10
#     return inner
# @decor1
# @decor2
# def return_num():
#     return 5
# print(return_num())
#
# # result = (decor(return_num))
# # print(result())
#-------------------------------------ობიექტზე ორიენტირებული პროგრამირება-------პითონი არის OOP -ენა-
#შევქმნათ Human კლასი და გადავცეთ პარამეტრები/მახასიათებლები, წიმაღლე და წონა.

class Human():
     height = 170
     weight = 60

     def __init__(self, name, age ):       #init -მეთოდი გვემსახურება რომ როგორც ობიექტი შეიქმნება შიდა პარამეტს შეუქმნის, როგორც კი ობიექტი იქმნება გვინდა ობიექტის შიდა პარამეტის შექმნა, გვინდა ფუნქცია რომელიც პარამეტს ავტომატურად შექმნის,ფუნქციებს რომლებმაც იციან როდი გაეშვან ვეძახით Magic ფუნქციებს/მეთოდებს.მიღებულია რომ კლასის პარამეტრების მერე დაიწეროს.
         self.name = name
         self.age = age

     @staticmethod
     def sleeping():                   #როდესაც გვინდა დავამატოთ მეთოდი, მეთოდი არის ფუნქცია რადგან აღნიშნავს ქმედებას, მაგ ძილი,სირბილი.
         print("ZzzzzzZzzzzzzz...")

     @classmethod
     def show_height(cls):
         print(f"human height is: {cls.height}")


     def say_hi(self):
         print(f"Hi My name is {self.name}")      #self -ში გადაეცემა ობიექტი. და ვინც იძახებს იმისი სახელი დაეწერება, თუ ჰუმან1 გამოიძახებს მისი და თუ ჰუმან2 მისი

     def __repr__(self):                          # repr მეჯიქ ფუნქციაში რეტარნში რასაც ჩაუწერ, ამოპრინტვისას იმას ამოპრინტავს.
         return f"Human ({self.name},{self.age})"


#ობიექტის შექმნა---------
Human1 = Human("Nika", 19)
Human2 = Human("Levani", 15)

print(Human1)
print(Human2)

# Human1.name = "Nika"
# Human2.name = "Elene"
# Human1.say_hi()
# Human2.say_hi()
#
# Human1.show_height()
# Human2.show_height()
# print(Human1.name)
# print(Human2.name)

#Human.show_height()
# #როდესაც სხვა ლაინზე მინდა კლასს ახალი პარამეტრი დავუმატო
# Human.hands_number = 2

# print(Human.hands_number)
# Human.sleeping()



