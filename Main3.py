# მორზეს კოდი ----------------------------------------------


a = "abcdefghijklmnopqrstuvwxyz"
b = ["._","_...","_._.","_..",".",".._.","__.","....","..",".___","_._","._..","__","_.","___",".__.","__._","._.","...","_",".._","..._",".__","_.._","_.__","__.."]

dictionary = {a[i]: b[i] for i in range(len(a))}
c = (input("enter your sentence: ")).lower()

converted_morse = '  '.join(dictionary.get(char, char) for char in c)

print("translated word:", converted_morse)


