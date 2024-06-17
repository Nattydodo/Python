Time = (input("Times table's number ="))
x = 1


if Time.isnumeric():
    Num = int(Time)
    while x<=12:
        
        print("%d " % int(Time) +"x "+"%d" % int(x) +" = "+"%d"% int(Num))
        x+=1
        Num+=int(Time)
else:
    print("Please Input a Number")
    