import os
os.system('cls')

def tri_func(num):
    #num = int(input("type the Number of Line you want to ptint:"))
    for i in range(1,num+1,):
        for j in range(1,i+1):
            print(j,end=' ')
        print()

print("End of the code")

tri_func(8)
###################################################################33
# Print the Output in reverse order
'''import os
os.system('cls')

num = int(input("type the Number of Line you want to ptint:"))
for i in range(num,0,-1):

    for j in range(1,i+1):
        print(j,end=' ')

    print()

print("End of the code")'''

