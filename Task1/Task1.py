userDay = int(input("enter day:"))
if userDay == 6 or userDay == 7:
    print("weekend")
elif userDay >= 1 and userDay <= 5:
    print("not weekend")
else:
    print("there is no such day")