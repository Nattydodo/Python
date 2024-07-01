def PointSum(W,M,F):
    sumS = W+M+F
    print("You got a total of " + "%d" %sumS +" score")
    return(sumS)

def Gradings(Pnt):
    if Pnt >= 80:
        print("You did outstanding!")
    elif Pnt >= 50:
        print("You passed")
    else:
        print("You failed")

WorkP = int(input("Enter Your Accumulative Score: "))
MidP = int(input("Enter Your Midterm's Score: "))
FinalP = int(input("Enter Your Final's Score: "))

if WorkP <= 20:
    if MidP <= 40:
        if FinalP <= 40:
            Gradings(PointSum(WorkP,MidP,FinalP))
        else:
            print("Score Exceed the limit of: Final Score")
    else:
        print("Score Exceed the limit of: Midterm Score")
else:
    print("Score Exceed the limit of: Accumulative Score")