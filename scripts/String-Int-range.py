""" # type the items to a range.
b=range(10,100,5)
###for i in b:
    ### print("values are",i)"""

#=============================#
"""val1=range(50,500,25)
#for i in val1:
 #   print("The items of these range are",i)"""

########################################
# print the range using len function.
g = range(50,500,25)

for i in range(len(g)): #as we are using len function here, we need range function also.
    print("The numbers are ", g[i])


##################################

#Nuber table

"""num = int(input("Write the number of your choise:"))
num2 = range(1,11)

for value in num2:
    #print(f'The table of {num} is as follows:')
    print(f'{num} * {value} = {num * value}')"""
    
###############################################################
#Nuber table in reverse order
'''num = int(input("Write the number of your choise:"))
num2 = range(10,0,-1)'''

'''for value in num2:
    #print(f'The table of {num} is as follows:')
    print(f'{num} * {value} = {num * value}')'''
#Collect an input from user and print all the letters of that input and count the Length of that string.     
'''b = input("Type some word of your chose:")
for i in b:
    print("The letters are",i)
print("The totla letters are in","b" ,len(b))'''
#Collect an input from user and print all the letters with the help of forloop using the Index with range option
'''b = input("Type some word of your chose:")
for i in range(len(b)):
    print("The letters are", b[i])
print("The totla letters are in","b" ,len(b))'''



