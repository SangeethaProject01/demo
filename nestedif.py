#nested if

##x=5
##y=3
##z=4
##
##if x<y:
##    if x<z:
##        print("x is smallest number",x)
##    else:
##        print("x is not smallest number")
##else:
##    print(" x is not a small number")

#match case

number=int(input("enter a number b/w 0 to 6:" ))

match number:
    case 0:
        print("monday",number)
    case 1:
        print("tuesday")
    case 2:
        print("wednesday")
    case 3:
        print("thursday")
    case 4:
        print("friday")
    case 5:
        print("saturday")
    case 6:
        print("sunday")
    case _:
        print("Invalid input")
    
        
