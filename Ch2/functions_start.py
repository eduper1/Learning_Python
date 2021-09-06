#
# Example file for working with functions
#

# define a basic function
def func():
    print("I am function")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1,arg2)

# function that returns a value
def cube(x):
    return x*x*x

# function with default value for an argument
def power(num, x=2):
    result = 1
    for i in range(x):
        result = result * num
    return result

#function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

func()
print(func())
print(func)
func2(10,10)
print(cube(2))
print(power(2))
print(power(2,2))
print(power(x=3, num=2))
print(multi_add(4,15,10,4))