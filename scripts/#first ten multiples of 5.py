#Question: 1 -first ten multiples of 5
'''a = range(0,11)
for i in a:
    print("first ten multiples of 5 is =", 5*i )'''

#Question: 2 - Print index 5 to Index 10 in the forward direction with help of slicing 
'''var="Artificial intelligence"
b = var[5:10]
print(b)'''

#Question: 6 - x=99, convert this as a string 

'''x=99
x_con =str(x)
print(x_con)
a= type(x)
b = type(x_con)
print("x is data type of", a)
print("x_con is data type of", b)'''

#Question: 9) print a given string in reverse order by slicing 

info="Artificial intelligence"
i1=range(-1, - (len(info)+1),-1)

'''i2 = info[::-1]
print(i2)'''

for i in i1:
    print(info[i])

'''a = input("Write a word:")
b = range(-1,-(len(a)+1),-1)

for i in b:
    print(f'{a[i]}')'''

a = input("Write a word:")

for i in range(-1,-(len(a)+1),-1):
    print(f'{a[i]}')




