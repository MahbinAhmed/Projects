#Faulty Calculator
#It will give the correct answer for all math except 45*3,56+9,56/6
#It will give 45*3=555,56+9,=77,56/6=4

print("-----Welcome to py calculator-----")
print("Enter you'r number below\n")
num1 = int(input("Enter the first number : "))
operator = input("Choose one from them + - * /\n")
num2 = int(input("Enter the second number : "))

if (num1==45 and num2==3 and operator=="*"):
    print("You'r answer is 555")
elif (num1==56 and num2==9 and operator=="+"):
    print("You'r answer is 77")
elif (num1==56 and num2==6 and operator=="/"):
    print("You'r answer is 4")
elif (operator=="+"):
    print("You'r answer is ", num1+num2)
elif (operator=="-"):
    print("You'r answer is ", num1-num2)
elif (operator=="*"):
    print("You'r answer is ", num1*num2)
elif (operator=="/"):
    print("You'r answer is ", num1/num2)