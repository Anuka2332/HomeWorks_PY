# ----N1 დავალება---------------------------------------
# list1 = []
# for i in range(1):
#     name1 = input("Enter Name: ")
#     last_name1 = input("Enter Last Name: ")
#     age1 = input("Enter your Age: ")
#     user_info = [name1, last_name1, age1]
#     list1.append(user_info)
#     y = ("Your entered Info", list1)
#     print(y)
# list2 = []
# for i in range(1):
#     name2 = input("Enter Name: ")
#     last_name2 = input("Enter Last Name: ")
#     age2 = input("Enter your Age: ")
#     user_info = [name2, last_name2, age2]
#     list2.append(user_info)
#     y = ("Your entered Info", list2)
#     print(y)
# list3 = []
# for i in range(1):
#     name3 = input("Enter Name: ")
#     last_name3 = input("Enter Last Name: ")
#     age3 = input("Enter your Age: ")
#     user_info = [name3, last_name3, age3]
#     list3.append(user_info)
#     y = ("Your entered Info", list3)
#     print(y)
#
#     z =[list1,list2,list3]
#     print(z)
#
#
#     user = int(input("Enter user index (1, 2, or 3): "))
#     if user == 1:
#         print(f"Name: {name1}")
#         print(f"Lastname: {last_name1}")
#         print(f"age: {age1}")
#     elif user == 2:
#         print(f"Name: {name2}")
#         print(f"Lastname: {last_name2}")
#         print(f"age: {age2}")
#     elif user == 3:
#         print(f"Name: {name3}")
#         print(f"Lastname: {last_name3}")
#         print(f"age: {age3}")
#     else:
#         print("Invalid user index")
#-------------N2 დავალებააააააა
# info = [
#     ("Audrey", "Hepburn", 64, ["Breakfast at Tiffany's", "Roman Holiday"]),
#     ("Angelina", "Jolie", 67, ["Kung Fu Panda", "MS & MR smith"]),
#     ("Tom", "Hiddleston", 39, ["Loki", "Thor"])
#     ]
#
# name = input("Enter actor's Name or Surname: ").lower()
#
# actor_found = False
#
# for actor in info:
#     if name.lower() in [actor[0].lower(), actor[1].lower()]:
#         actor_found = True
#         print("Actor found:")
#         print("Name:", actor[0], actor[1])
#         print("Age:", actor[2])
#         print("Nationality:", actor[3])
#         break
#
# if not actor_found:
#     print("Actor not found.")
#-------------------------N3 დავალება
# def unique_list(x):
#     unique_set = set(x)
#     unique_list = list(unique_set)
#     return unique_list
#
# x = [1,2,3,3,3,4,5,5,6,7,8,8,8,9,10]
# result = unique_list(x)
# print(result)

#----------N4 დავალება----------------

# def set_union(x, y):
#     result = set.union(x, y)
#     return result
#
# x = {1, 2, 3, 4, 5}
# y = {8, 3, 9, 5, 7}
# print(set_union(x, y))
#
# N 5 ---დავალება--------------------
# def check_dict(dictionary):
#     if len(dictionary) == 0:
#         print("Dictionary is empty.")
#     else:
#         print(dictionary)
#
# # dictionary = {}
# dictionary= {"ana": 1, "bela": 2, "gela": 3}
# check_dict(dictionary)

#N 6 დავალება-------------------------------------
def count_characters(count):
    dictionary = {}
    for char in count:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary

count = input('Enter sth: ')
print(count_characters(count))


