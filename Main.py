# Lesson 1 ----------------------------------------------------------------------------------------

# print(input("What is your name?"),input("What is your surname?"))

# A = int(input("First Number"))
# B = int(input("Second Number"))
# print(A**B)

# input("Name:")
# input("Surname:")
# input("Age:")
# input("City")

# A = input("Fruit 1")
# B = input("fruit 2")
# C = input("fruit 3")
# print(A+"//"+B+"%%"+C)

# A = input("count The Symbols:")
# print(len(A))

#Lesson 2 --------------------------------------------------------------------------------------

# answer = input("are you Elene? (yes/no)")
# if answer == "yes" or answer == "Yes:"
#     answer1 = input ("How are you?").lower()
#     if answer1=="good":
#         print("I'm Happy")
#     else:
#         print("...")
#
# elif answer == "no" or answer =="No":
#     print("Goodbye")
# else:
#     print("Can not understand")

#1..................................saklaso davaleba
# answer = input("What is your name?").lower()
# if answer == "bond":
#     print("welcome on board 007")
# else:
#     print("Good Morning",answer)

#........................

# i = 0
# while i < 10:
#     i = i + 1
#     if i == 8:
#         continue
#     print(i)
# else:
#     print("finished")
#..........................

# a = "How are you?"
# for i in a:
#     if i != " ":
#         print(i)
#.......................... 1 dan daiwyebs da 2 is gamotovebiT dawers 10 mde
# for i in range(1,10,2):
#         print(i)
#.................................წამოიღოს ის ნომერი სიმბოლო რომელსაც ვეტყვი, სლაისინგი, დაჭრა... მე-0 დან დაიწყოს მე-4 დან 2ც.
# a = "television"
# print(a[0:4:2])
#.................................მაქვს ი ცვლადი რომელიც მინდა 1 დან 100 მდე შეიცვალოს და ერთმანეთზე გადამრავლდეს
# for i in range (1,101):
#     for j in range (1,101):
#         print(f"{i}*{j}=", i * j)
#     print(' ')
#-----------------------------------------savarijso 2
#მომხმარებელს პროგრამა სთხოვს წლოვანების შეყვანას და 18  წლის ზემოთ გამოაქ მესიჯი რომ შეუძლია არჩ. მონაწ
# a = int(input("what is your age?"))
# if a >= 18:
#     print("you can vote")
# else:
#     print("you can't vote")
#მომხმარებელს პროგრამა სტხოვს ორი რიცხვის შეყვანას და აბრუნებს უმცირესს
# a = int(input("write First number"))
# b = int(input("write second number"))
# if a < b:
#     print(a)
# else:
#      print(b)
# პროგრამა სტხოვს მომხმარებელს სამ მთელ რიცხვს და ბეჭდავს მათ შორის უდიდესს.
# a = int(input("write First number"))
# b = int(input("write second number"))
# c = int(input("write Third number"))
# if a > b and a > c:
#     print(a)
# elif b > a > c:
#     print (b)
# else:
#     print(c)
# პროგრამა სთხოვს მომხმარებელს შეიყვანოს მთელი რიცხვი და ამოწმებს იყოფა თუ არა შეყვანილი რიცხვი 2-ზე და 3-ზე. შემდეგ ბეჭდავს შესაბამის მესიჯს.
# a = int(input("Enter Number"))
# if a % 2 == 0 and a % 3 == 0:
#     print ("it's devided")
# ჯეირანის კოდი ----------------------------------
# from random import choice
# a = ["paper", "scissors", "rock"]
# human = 0
# computer = 0
#
# while True:
#     human_answer = input(f"enter your choice {a}:")
#     if human_answer in a:
#         break
#     print ("incorrect!")
#
# human_answer = input(f"enter you choice {a}:")
# computer_answer = choice(a)
# print(human_answer, computer_answer)
# if human_answer == computer_answer:
#     print("tie")
# elif (human_answer == "scissors" and computer_answer == "rock") or (human_answer == "paper" and computer_answer == "scissors") or (human_answer == "rock" and computer_answer == "paper"):
#     computer += 1
#     print("human is defeated!")
# else:
#     human += 1
#     print("computer is defeated!")

# დავალება 2

#ვიქტორინა ---------------------------------------------------------------------------------------------------

# b = ["1.შუმერთა", "2.სელჩუკთა", "3.რომის", "4.მონღოლთა"]
# a = str(input(f"რომელი იმპარიის მიერ აგებული წყალ-მომარაგების სისტემა(აკვედუკი) ფუნქციონირებს დღესაც?{b}:"))
# print(a)
# if a == "რომის" or a == "3":
#     print("სწორია!")
# else:
#     print("არა! სწორი პასუხია რომის!")

# გამრავლების ტაბულა -----------------------------------------------------------------------------------------

# a = int(input ("Enter Number"))
# for i in range (1,a+1):
#     for j in range (1,a+1):
#         print(f"{i}*{j}=", i * j)
#     print(' ')

# თუთიყუშის პროგრამა -----------------------------------------------------------------------------------------

# while True:
#     a = input ("user said whaaat!?")
#     if a == "quit":
#         break
#     else:
#         print(f"User seid {a}:")

#ონლაინ მაღაზია -----------------------------------------------------------------------------------------------

# a = {"Leptops","PC","Mobile"}
# b = input(f"choose only one category:{a}:")
#
# #Products Category
# Leptops = ["Hp", "MacBook", "Lenovo"]
# PC = ["Samsung", "Apple", "acer"]
# Mobile = ["Samsung galaxy s21", "Iphone 12" "xiaomi"]
# if b == "Leptops":
#     print(Leptops)
# elif b == "PC":
#     print(PC)
# elif b == "Mobile":
#     print(Mobile)
# else:
#     print("There is not such category")
# #about budget
# c = int(input("enter your max budget:"))
#
# Leptops = 3500
# PC = 2500
# Mobile = 1500
# if b == Leptops and c >= 3500
#
# if c < 1500:
#     print("I have no offer in this amount")
# elif c >= 1500 and b < 2500:
#     print("Mobile")
# elif c >= 2500 and b < 3500:
#     print("PC")
# elif c >= 3500:
#     print("leptops")

#3 leqcture ----------ყველა ფუნქცია აბრუნებს რაღაცას თუ არ ვეტყვი რა დააბრუნოს დააბრუნებს none---------------------------------------------------------------------------------------
#იმისთვის რომ მათე,ატიკური ფუნქციები გამოვიტანოთ უნდა შემოვიტანოთ მათემატიკის მოდული რახან, წვდომა მიეცეს და დაინახოს
# import math
# a = math.factorial(6)
# print(a)
#-----------------------------------------ფუნქციის შექმნა---------
# def say_hi(name):
#     return f"Hi {name}!"
#
# a = input("enter your name: ")
# returned_string = say_hi(a)
# print(returned_string)
#--------------------------------გლობალური ცვლადის დარედაქტირება ლოკალში-----------
# x = 100
# def show_x():
#     y = 11
#     def inner():
#         n = 5
#         print(n)
#     return inner
# #
# show_x()()
#----------------------ლამბდა ფუნ1ქცია არის უსახელო ფუნქცია და რამდენ პარამეტრსაც მინდა იმდენს გადავცემ, ოღონდ ეს უნდა შევინახო რამე ცვლადში
# x = lambda a, b: a + b
# print(x(2,3))
#--------------------სიები- სპლიტს სეპატარორად ()ში ავტომატურად სფეისი აქვს მაგრამ შემიძლია სხვა რამ მივუთითო(",")ასე.
# a = "Hi my name is Ana"
# b = a.split()
# print(len(b))
#--------------------------- რანდომ რიცხვი ჩაიფიქროს კომპმა და ნელ ნელა მივიდეთ სწორ პასუხამდე
# from random import randint
# def guess_number (myrange):
#     num = randint(1,myrange)
#     i = 0
#     while True:
#         i += 1
#         answer = int(input(f"I have choosen one number in range 1-{myrange}, guess which: "))
#         if answer == num:
#             print(f"correct, you needed {i} tries to guess")
#             break
#         elif answer < num:
#             print("My number is greater")
#         else:
#             print("mu number is less")
# guess_number(5)
#---------------X 0 თამაში--------
table = ["?", "?", "?",
          "?", "?", "?",
          "?", "?", "?"]

#იმისთვის რომ დავხაზოთ სათამაშო არეალი გავაკეთებ ფუნქციას.
def display_table():
    """პრინტავს ტერმინალში თეიბლს"""
    print(table[0] + "|" + table[1] +"|" + table[2] + "                 " + "1|2|3")
    print(table[3] + "|" + table[4] +"|" + table[5] + "                 " + "4|5|6")
    print(table[6] + "|" + table[7] +"|" + table[8] + "                 " + "7|8|9")

#მეორე ფუნქცია გავაკეთოთ რომ ფლეიერმა აირჩიოს x ყავდეს თუ 0.....
def players ():
    """ირჩევს ფლეიერს"""
    print("choose Player X / 0 ")
    player1 = input("player1: ")
    player2 = " "
    if player1 == "X":
        player2 = "0"
        print(f"player2: {player2}")
    elif player1 == "0":
        player2 = "X"
        print(f"player2: {player2}")
    else:
        print("Invalid input!")
# ეხლა შევქმნათ გლობალური ცვლადები
current_player = "X"
run = True

def player_position():
    """ირჩევს პოზიციას X-ს ან 0-სთვის"""
    global run
    print("Current Player: " + current_player)
    position = input("Choose 1/9: ")

    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input ("Choose 1/9: ")
        position = int(position) - 1

        if table[ position] == "?":
            valid = True
        else:
            print("Possition is taken!")

    table [position] = current_player
    display_table()
# მჭირდება ახალი ფუნქცია რათა დავწერო როდის შეიცვლება ქარენთ ფლეიერი როდის გახდრს 0 და როდის X
def flip_player():
    """ცვლის ფლეიერს"""
    global current_player
    if current_player == "X":
        current_player = "0"
    else:
        current_player = "x"

# ხომ უნდა გადავამოწმოტ ვინ გაიმარჯვებს, და გვინდა ავალი ფუნქცია
def check_winner():
    """ამოწმებს ვინ მოიგო"""
    global run
    if table[0] == table[1] == table[2] !="?":
        run = False
        print(table[0] + "WON!")
    elif table[3] == table[4] == table[5] !="?":
        run = False
        print(table[3] + "WON!")
    elif table[6] == table[7] == table[8] !="?":
        run = False
        print(table[6] + "WON!")
    elif table[0] == table[3] == table[86] !="?":
        run = False
        print(table[0] + "WON!")
    elif table[1] == table[4] == table[7] !="?":
        run = False
        print(table[1] + "WON!")
    elif table[2] == table[5] == table[8] !="?":
        run = False
        print(table[2] + "WON!")
    elif table[0] == table[4] == table[8] !="?":
        run = False
        print(table[0] + "WON!")
    elif table[2] == table[4] == table[6] !="?":
        run = False
        print(table[2] + "WON!")
    elif "?" not in table:
        run = False
        print("Tie!")


#ეხლა დაგვრჩა 1 ფუნქცია, თვითონ თამაშის ფუნქცია სადაც ყველა ფუნქცია გაერთიანდება
def play_game():
    """იწყებს თამაშს"""
    print("TicTacToe Starts!")
    display_table()
    players()

    while run:
        player_position()

        flip_player()

        check_winner()
play_game ()

#N3 კალკულატური---------ეს წასაშლელიააააააააააააააააააააააააააააააააა
# def calculator(calculate):
#     return (f"solution {calculate}")
#
#     a = int(input("What is First Number? "))
#     b = int(input("What is second Number? "))
#     c = (input("Select an operation (*, /, +, -, ^ ): "))
#
#     if c == "/" and b == 0:
#         print("Cannot divide by zero")
#     elif c == "/":
#         print(a/b)
#     elif c == "*":
#         print(a*b)
#     elif c == "+":
#         print(a+b)
#     elif c == "-":
#         print(a-b)
#     elif c =="^":
#         print(a^b)
#     else:
#         "choose correct operation"
#
# calculator()

#--------------- მორზეს ანბანი----------------------------------

a = "abcdefghijklmnopqrstuvwxyz"
b = ["._","_...","_._.","_..",".",".._.","__.","....","..",".___","_._","._..","__","_.","___",".__.","__._","._.","...","_",".._","..._",".__","_.._","_.__","__.."]

dictionary = {a[i]: b[i] for i in range(len(a))}
c = (input("enter your sentence: ")).lower()

translated_word = '  '.join(dictionary.get(char, char) for char in c)

print("translated word:", translated_word)

# for i in range (len(c)):
#     print(a[i],b[i])