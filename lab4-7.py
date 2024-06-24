def BMI(w,h):
    BB = w/h**2
    
    return(BB)

def Compare(BB):
    
    print("BMI = %0.2f " %BB)

    if BB>30:
        print("อ้วนมาก/โรคอ้วนระดับ 3")
    elif BB>25 and BB<29.90:
        print("อ้วน/โรคอ้วนระดับ 2")
    elif BB>23 and BB<24.90:
        print("ท้วม/โรคอ้วนระดับ 1")
    elif BB>18.50 and BB<22.90:
        print("ปกติ (สุขภาพดี)")
    else:
        print("น้ำหนักน้อย/ผอม")

kg = float(input("Weight(kg) = "))
m  = float(input("Height(cm) = "))

m = m/100

Compare(BMI(kg,m))
