"""
list overlap
"""
a=[1,2,3,4,5,6,7,8,9,10]
b=[1,3,5,7,9]
c=[]
for i in a and b:
    if i in a and b:
        c.append(i)
        print(c)
