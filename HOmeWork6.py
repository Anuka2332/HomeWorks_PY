from abc import ABC,abstractmethod
class Country(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def population(self):
        pass
    @abstractmethod
    def budget(self):
        pass

    @staticmethod
    def we_are():
        print("Georgia is European Country")

class Georgia(Country):
    def area (self):
        print("The area of Georgia is 69,700 km²")

    def population(self):
        print("The population of Georgia is 3.713 Millin")

    def budget(self):
        print("The 2024Y budget of Georgia is 22 Billion")


georgia = Georgia()
georgia.area()
georgia.budget()
georgia.population()
georgia.we_are()

