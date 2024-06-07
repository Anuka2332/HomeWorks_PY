# დავალება 3 --------
# N1 შექმენით ფუნქცია რომელიც მომხმარებლისგან მიიღებყლ ინფორმაციას გაასამმაგებს-----------
# def tripling_data():
#     a = input("Enter Word: ")
#     print (f"Tripled:" + a * 3)
# tripling_data()
#N2 შექმენით ფუნქცია რომელიც მომხმარებლისგან წონას და დააბრუნებს მთვარეზე-----------
# def count_on_the_moon (weight):
#     return (f"Your weight On the Moon is {weight / 6} kg!")
#
# a = int(input("Enter your weight: "))
# print (count_on_the_moon (a))
#N3 კალკულატური---------
# def calculator():/
#     a = int(input("What is the First Number? "))
#     b = int(input("What is the Second Number? "))
#     c = input("Select an operation (*, /, +, -, ^ ): ")
#
#     if c == "/" and b == 0:
#         return "Cannot divide by zero"
#     elif c == "/":
#         return a / b
#     elif c == "*":
#         return a * b
#     elif c == "+":
#         return a + b
#     elif c == "-":
#         return a - b
#     elif c == "^":
#         return a ** b
#     else:
#         return "Choose correct operation"
#
# result = calculator()
# print("Solution:", result)
# მორზეს კოდი ----------------------------------------------


a = "abcdefghijklmnopqrstuvwxyz"
b = ["._","_...","_._.","_..",".",".._.","__.","....","..",".___","_._","._..","__","_.","___",".__.","__._","._.","...","_",".._","..._",".__","_.._","_.__","__.."]

dictionary = {a[i]: b[i] for i in range(len(a))}
c = (input("enter your sentence: ")).lower()

converted_morse = '  '.join(dictionary.get(char, char) for char in c)

print("translated word:", converted_morse)
