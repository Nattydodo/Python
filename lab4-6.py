def Cir(r):
    area = (22/7)*(r**2)
    return area

Radius = float(input("Radius = "))
Answer = Cir(Radius)

print("Your Area Is: "+ str(Answer))