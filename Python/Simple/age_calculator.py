# Problem-1 (Easy)

def age_needed_for_100(age):
    a = 100-age
    return a

def birthyear_from_age(age):
    a = 2021-age
    return a

first_input = int(input("Enter your age or year of birth : "))
second_input = input("Press y to add a particular year or press n : ")

if second_input == "n":
    if first_input > 1500 and first_input < 2021:
        print(f"Your age will trun into 100 in {first_input+100}")

    elif first_input > 2021:
        print(f"You haven't born yet. ")

    elif first_input < 100 :
        a = age_needed_for_100(first_input)
        print(f"Your age will turn into 100 in {2021+a}")

    elif first_input >= 100:
        print(f"You have already been turned into 100")

    else :
        print("Enter a number.")

elif second_input == "y":
    particular_year_input = int(input("Enter the year : "))
    if first_input > 1500 and first_input < 2021:
        print(f"Your age will turn into 100 in {first_input+100}")
        print(f"In {particular_year_input} your age will turn into {particular_year_input-first_input}")

    elif first_input > 2021:
        print(f"You haven't born yet. ")

    elif first_input < 100 :
        a = age_needed_for_100(first_input)
        print(f"Your age will turn into 100 in {2021+a}")
        b = birthyear_from_age(first_input)
        print(f"In {particular_year_input} your age will turn into {particular_year_input-b}")

    elif first_input >= 100:
        print(f"You have already been turned into 100")
        a = birthyear_from_age(first_input)
        print(f"In {particular_year_input} you age will turn into {particular_year_input-a} ")

    else:
        print("Print enter a number")

else:
    print("Enter between 'y' and 'n' ")