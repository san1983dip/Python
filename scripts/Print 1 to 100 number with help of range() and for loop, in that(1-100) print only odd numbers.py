#Print 1 to 100 number with help of range() and for loop, in that(1-100) print only odd numbers

a = range(1,101)
          
for i in range(len(a)):
    if (i%2 != 0):
        print(f"The odd numbers of the given {a} are as follows {i}")
