def ask(number):
    time = 1
    sum = 0
    while int(time) <= int(number):
        sum += int(input( "student no." + "%d"  %time + "'s score: "))
        time += 1
    return (sum)


n = input("Input the number of students: ")
avg = int(ask(n))/int(n)
print("The average is: " + "%d" %avg)