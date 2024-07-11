#Astrologer's Stars

while(True):
    print("Enter 1 for normal printing or enter 2 for reverse printing")
    b = int(input())
    a = int(input("Enter the ammount of the last stars : "))

    if b == 1:
        for i in range(0,a+1):
            print(i * "*")
        break

    elif b == 2:
        for i in range(a,0,-1):
            print(i*"*")
        break

    else:
        print("You have entered wrong number. Please enter 1 or 2")
        continue

print("Thanks for printing patterns")