# 
# Example file for variables
#

# Declare a variable and initialize it
f = "abc"
print(f)


# re-declaring the variable works
f = 0 
print(f)


# ERROR: variables of different types cannot be combined
print("This is string" , 123)


# Global vs. local variables in functions
def someUnc():
    global f
    f = "def"
    print(f)
    
someUnc()
print(f)

del f
print(f)