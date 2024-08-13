#print all factors of given number 
num=int(input("Type a number of your choise: "))

for i in range(1,num+1):
    if num % i ==0:
        print(f"One of factors of {num} is {i}")
print('Congrats, You go the result')