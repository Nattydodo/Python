Score = (input("Your score = "))

if Score.isnumeric():
    if int(Score) >= 0 and int(Score) <= 100:

        if int(Score) > 80:
            print("เกรด A")
        elif int(Score) > 70:
            print("เกรด B")
        elif int(Score) > 60:
            print("เกรด C")
        elif int(Score) > 50:
            print("เกรด D")
        else:
            print("เกรด F")

    else:
        print("กรุณากรอกข้อมูล 0-100")
else:
    print("กรุณากรอกข้อมูล 0-100")