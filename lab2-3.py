H = float(input("Hight(cm) = "))
W = float(input("Wight(kg) = "))

BMI = float(W/((H/100)**2))

print("BMI = " + "%.2f" % BMI)
if BMI>30:
    print("อ้วนมาก/โรคอ้วนระดับ 3")
elif BMI>25 and BMI<29.90:
    print("อ้วน/โรคอ้วนระดับ 2")
elif BMI>23 and BMI<24.90:
    print("ท้วม/โรคอ้วนระดับ 1")
elif BMI>18.50 and BMI<22.90:
    print("ปกติ (สุขภาพดี)")
else:
    print("น้ำหนักน้อย/ผอม")