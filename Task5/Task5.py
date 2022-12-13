userQuarter = int(input("enter quarter:"))

if userQuarter == 1:
    print("x > 0 and y > 0")
elif userQuarter == 2:
    print("x < 0 and y > 0")
elif userQuarter == 3:
    print("x < 0 and y < 0")
elif userQuarter == 4:
    print("x > 0 and y < 0")
else: print("you enered an incorrect quarter")