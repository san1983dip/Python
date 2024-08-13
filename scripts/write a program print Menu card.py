'''4) write a program print Menu card like
		step:-1
		-------
		1. add
		2. sub
		3. mutliplication
		4. division
		(print it by using print() function)

		step-2
		------
		take an input from the user as integer from 1-4

		step-3(if-elif-elif-elif-elif-else)
		------
		check user provided value if it is 1 => take again two inputs do the sum
		check user provided value if it is 2 => take again two input do the subtract
		check user provided value if it is 3 => take again two input do the multiplication
		check user provided value if it is 4 => take again two input do the division
		check user provided invalid value(not 1 to 4) => print invalid input'''
print("-------")
print("1. add")
print("2. sub")
print("3. multiplication")
print("4. division")
a = int(input("Type a number between 1-4 to specify your action:"))
a1 = int(input("Type any number "))
a2 = int(input("Type anyothernumber "))

if (a==1):
    a3 = a1+a2
    print(f"your fisr choise was {a},and result is {a3}")
elif (a==2):
    a3 = a1-a2 
    print(f"your fisr choise was {a},and result is {a3}")
elif (a==3):
    a3 = a1*a2 
    print(f"your fisr choise was {a},and result is {a3}")
elif (a==4):
    a3 = a1/a2 
    print(f"your fisr choise was {a},and result is {a3}")

else:
    print("Selection is out of range")

#######################################################################################################
#another process:
print("-------")
print("1. add")
print("2. sub")
print("3. multiplication")
print("4. division")
a = int(input("Type a number between 1-4 to specify your action:"))


if (a==1):
    a1 = int(input("Type any number "))
    a2 = int(input("Type anyothernumber "))
    a3 = a1+a2
    print(f"your fisr choise was {a},and result is {a3}")
elif (a==2):
    a1 = int(input("Type any number "))
    a2 = int(input("Type anyothernumber "))
    a3 = a1-a2 
    print(f"your fisr choise was {a},and result is {a3}")
elif (a==3):
    a1 = int(input("Type any number "))
    a2 = int(input("Type anyothernumber "))
    a3 = a1*a2 
    print(f"your fisr choise was {a},and result is {a3}")
elif (a==4):
    a1 = int(input("Type any number "))
    a2 = int(input("Type anyothernumber "))
    a3 = a1/a2 
    print(f"your fisr choise was {a},and result is {a3}")

else:
    print("Selection is out of range")
