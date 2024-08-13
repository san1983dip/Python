#write a function with variable length arguments for finding the average of the given numbers 
def avg_func(*args):
    a = sum(args) / len(args)
    print("The avarage of given number is",a)
avg_func(10,20,30,40)

