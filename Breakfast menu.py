"""
Application: Breakfast menu
Written by: jhew86
"""
print("please select a number from the following items")
print("1 eggs")
print("2 waffles")


choice=float(input("what is your choice?"))

if choice==1:
    print("you chose eggs")
    print("choose your side")
    print("1 white toast")
    print("2 whole wheat toast")
    bread=float(input("what is your choice"))
    if bread==1:
        print("white toast")
        print("you chose option ", choice, "and option ", bread)
    else:
        print("whole wheat toast")
        print("you chose option ", choice, "and option ", bread)
elif choice==2:
    print("you chose waffles")
    print("choose a topping")
    print("1 syrup")
    print("2 strawberries and cream")
    topping=float(input("what is your choice"))
    if topping == 1:
        print ("syrup")
        print("you chose option ", choice, "and option ", topping)
    else:
        print("strawberries and cream")
        print("you chose option ", choice, "and option ", topping)
else:
    print("incorrect value selected. please try again")
    
        
   
          
    
