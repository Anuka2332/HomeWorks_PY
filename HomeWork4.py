class Transport():     #1. ტრანსპორტის კლასი მინ 4 პარამეტრით
    wheel = 4
    steering_wheel = 1
    door = 4
    seat = 5

    def __init__(self, name, year, km):   #4. მეჯიქ მეთოდი init მინ 3 პარამეტრით.
        self.name = name
        self.year = year
        self.km = km

    @staticmethod        # 2. 1 სტატიკური მეთოდი
    def mooving():
        print("direction to...")

    @classmethod          #3. 2 კლასის მეთოდი
    def wheel_are(cls):
        print(f"Transport has wheels: {cls.wheel}")

    @classmethod           #3. 2 კლასის მეთოდი
    def doors_are(cls):
        print(f"Transport has doors: {cls.door}")
# Transport.wheel_are()
# Transport.doors_are()

    def my_car(self):                                 #5. მინიმუმ 2 ობიექტის მეთოდი, ეს ერთი
        print(f"My Car Is {self.name}")


    def Year_car(self):                                #5. მინიმუმ 2 ობიექტის მეთოდი, ეს მეორე
        print(f"Year of My Car is {self.year}")


    def __repr__(self):
        return f"Transport ({self.name},{self.year},{self.km})"   #6. repr მეჯიქ მეთოდი


Transport1 = Transport("jeep", 2019, 10000)     #7. კლასისგან მინ 5 ობიექტის შექმნა
Transport2 = Transport("Mersedes", 2018, 12000)
Transport3 = Transport("Nissan", 2016, 14000)
Transport4 = Transport("Bentley", 2023, 0)
Transport5 = Transport("Ferrari", 2022, 5000)




print(Transport1)
print(Transport2)
print(Transport3)
print(Transport4)
print(Transport5)


Transport1.my_car()
Transport2.Year_car()

Transport.mooving()

