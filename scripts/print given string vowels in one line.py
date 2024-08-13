 #print given string vowels in one line and consonants in one line

s = input("Type some words of your choise:")
vowels = "aeiouAEIOU"
for i in s:
    if i.isalpha():
        if i in vowels:
            print(f"these are vowels of given input = {i}")
        else:
            print(f"these are consonenets of given input = {i}")

    