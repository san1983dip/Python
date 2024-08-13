#1) define a function with 2 position parameter. And call it by with help of position arguments and keyword arguments and combination

def posi_func(a,b):
    print("Sum of=",a+b)
    print("Product is =", a*b)
print("Calling by position arguments")
posi_func(10,20)
print("*"*40)
print("Calling by keyword argument")
posi_func(a=30,b=50)
print("*"*40)
print("Calling by keyword+position argument combination")
posi_func(10,b=50)

