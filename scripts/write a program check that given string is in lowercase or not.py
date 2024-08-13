#write a program check that given string is in lowercase or not ?

a = input("Write any word:")

if a.islower() == 1:
    print(f'The given value {a} is in lower case')
else:
    print (f'The given value {a} is not comptetly in lower case')
