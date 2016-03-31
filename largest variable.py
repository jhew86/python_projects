"""
Max of three
"""
#this is an exercise from practicepython.org
#this function takes input for three variables
#and prints the largest of the three.

def largest_var(x, y, z):
    if x > y and z:
        print(x)
    elif y > z:
            print(y)
    else:
        print(z)
        
