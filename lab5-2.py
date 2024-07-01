def price(num):

    i = 1
    sum = 0
    while i <= num:
        sum += int(input("Enter the product no." + "%d" %i + "'s price: "))
        i += 1
    return(sum)

def Vat(tot):
    Vated = tot + (tot*0.07)
    return(Vated)
    
def Pay(pp,cost):
    change = pp - cost
    return(change)


ProductN = int(input("Enter product's amount: "))
Total = price(ProductN)
SubTotal = Vat(Total)
print("The SubTotal (VAT7%) is: " +"%d" %SubTotal)
Paied = int(input("Enter the paied amount: "))
Change = Pay(Paied,SubTotal)

if Change<0:
    print("Insufficient amout")
else:
    print("Your change is: " + "%d" %Change)

