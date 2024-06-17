# class Person:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#
#     def introduction(self):
#         print(f"Hi, my name is {self.firstname}")
# class Georgian:
#     def __init__(self, location):
#         self.location = location
#     @staticmethod
#     def say_hi():
#         print("გამარჯობა")
#
# class Student(Person, Georgian):           ##მემკვიდრეობით გადავეცი პერსონი ასევე აქ შემიძლია დამატებითი ფუნქციონალის ჩაწერა
#     def __init__(self, firstname, lastname, subject, location):
#         # super(). __init__(firstname,lastname)          ##მშობელ კლასს ასე გადავცემ, სუპერში იგულისხმება მშობლის კლასი, როცა რამდნეიმე მშობელი მყავს სუპერად მიიჩნევს პირველს
#         Person. __init__(self, firstname,lastname)      ##ასე სახელს დავწერ წერტილს და ჩამოვთვლი სელფში რაც აქვს თუ რამდენიმე მშობელია მის ქვემოთ ჩამოვწერ იგივენაირად ყველას.
#         Georgian.__init__(self,location)
#         self.subject = subject
#
#
#     def show_profession(self):
#         print(f"I study {self.subject}")
#
#
# student1 = Student("Nino", "Khorguani", "biology","Tbilisi")
# student1.show_profession()
# student1.introduction()
# student1.say_hi()
# print(student1.location)
##-------------------------------------
# class Person:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#
#     def introduction(self):
#         print(f"Hi, my name is {self.firstname}")
#
#
# class Student(Person):
#     def __init__(self, firstname, lastname, subject):
#         # super().__init__(firstname, lastname)
#         Person.__init__(self, firstname, lastname)
#         self.subject = subject
#
#
#     def show_profession(self):
#         print(f"I study {self.subject}")
#
#
# student1
#---------პოლიმორფიზმი---- ყველა კლასში ერთნაირი სახელები აქვს მეთოდებს მაგრამ სხვადასხვა რაღაცას პრინტავენ ესაა პოლიმორფიზმი, სადაც შემიძლია მშობლისგან გადმოცემული მემკვიდრეობა შევცვალო-------------
#
# class Base:
#     def __init__ (self, brand, model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("General Movement...")
#
# class Boat(Base):
#     def move(self):
#         print("sail")
#
# class Car(Base):
#     def move(self):
#         print("Drive")
#
#
# class Plain(Base):
#     def move(self):
#         print("Fly")
#
#
#
# car = Car("BMW", "X5")
# boat = Boat("Yacht", "7788")
# plain= Plain("Boing", "AH15")
#
# car.move()
# boat.move()
# plain.move()

#--------------------------------აბსტრაქტული კლასები---როცა ვქმნით კლასს სხვა კლასების შესაქმნელად და არა ობიექტების შესაქმნელად-აბსტრაქტული კლასისგან არ შეიძლება ობიექტის შექმნა.--
#--- მაგალითად რამდენიმე კლასი შევქმნათ რომელიც გეობემტრიულ ფიგურებს განასახიერებენ
# ამისთვის შეიძლება 1 მშობელი შევქმნა რათა გავწერო რომ ყველას აქვს პერიმეტრი ფართობი და ა.შ..
# იმისთვის რომ კლასი იყოს აბსტრაქტული შიგნით უნდა ჰქონდეს მინ 1 აბსტრაქტული მეთოდი
# from abc import ABC, abstractmethod
# class Polygon(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#     @abstractmethod
#     def area(self):
#         pass
#
#     @staticmethod
#     def introduction():
#         print("I'm Geometric Figure!")
#
#
# class Triangle(Polygon):
#     def perimeter(self):
#         print("Calculate Triangle Perimeter: a+b+c")
#     def area (self):
#         print("Calculate Triangle Area: H*a/2")
#
# class Rectangle(Polygon):
#     def perimeter(self):
#         print("Calculate Triangle Perimeter: a+b+c+c")
#     def area (self):
#         print("Calculate Triangle Area: a*b")
#
# class Circle(Polygon):
#     def perimeter(self):
#         print("Calculate Triangle Perimeter: 2*p*r")
#     def area (self):
#         print("Calculate Triangle Area: p*r^2")
#
#
#
# triangle = Triangle()
# triangle.perimeter()
# triangle.area()
# triangle.introduction()
#
# rectangle = Rectangle()
# rectangle.perimeter()
# rectangle.area()
# rectangle.introduction()
#
# circle = Circle()
# circle .perimeter()
# circle .area()
# circle .introduction()
#----------------------------iiiiiiiisssssseeeeeeeeeeeeeeeee-------
# import turtle
# t = turtle.Turtle()
#
# t.up()               #ამის დაწერის მერე არ დახატავს და გადაადგილდება
# t.goto(0,-200)     # X და Y ღერძზე მიმაართულებას ვეუბნები
# t.down()                #ამის დაწერის მერე დახატავს
# t.circle(100)
# t.up()
# t.goto(0,0)
# t.down()
# t.circle(30)
# t.up()
# t.goto(0,0)
# t.down()
# t.goto(-90,-70)
# t.goto(0,0)
# t.down()
# t.goto(-60,-70)
# t.goto(0,0)
# t.down()
# t.goto(-30,-90)
# t.goto(0,0)
# t.down()
# t.goto(-10,-90)
# t.goto(0,0)
# t.down()
# t.goto(20,-80)
# t.goto(0,0)
# t.down()
# t.goto(50,-70)
# t.goto(0,0)
# t.down()
# t.goto(90,-70)
#-----------------------Heart-----
# import turtle
# t = turtle.Turtle()
# t.color("red")
# t.begin_fill()
# t.fillcolor("red")
# t.up()
# t.goto(0,-50)
# t.down()
# t.left(140)
# t.forward(180)
# t.circle(-90,200)
# # t.left(120)      #ამიტაც შეეძლო მიმართულების შეცვლა
# t.setheading(60)   #მიმართულება შეცვალა ამით
# t.circle(-90,200)
# t.forward(180)
# t.end_fill()
# turtle.done()
#-----------------------khinkali---------------
import turtle
t = turtle.Turtle()

t.up()
t.goto(0,-60)
t.down()
t.left(180)
t.forward(100)
t.circle(-90,95)
t.setheading(60)
t.circle(-155,70)
t.forward(15)
t.circle(-160,50)
t.setheading(-110)
t.circle(-150,56)


t.up()
t.goto(-44,109)
t.down()
t.circle(-25, steps=7)

t.up()
t.goto(-55,120)
t.down()
t.goto(-170,30)
t.goto(-55,120)
t.down()
t.goto(-100,0)
t.goto(-55,120)
t.down()
t.goto(-20,0)
t.goto(-55,120)
t.down()
t.goto(50,5)
t.goto(-55,120)






turtle.done()