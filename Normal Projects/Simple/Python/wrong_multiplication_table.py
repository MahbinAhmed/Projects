# Problem-8

# Modules
import random

# Module
import random

# Function_section
def multiplication_table(number):
    multiplication_table_list = []
    for i in range (1,11):
        a = number*i
        multiplication_table_list.append(a)
    wrong_result = random.randint(1,9)
    multiplication_table_list[wrong_result] = multiplication_table_list[wrong_result]+random.randint(1,3)
    return multiplication_table_list

def verifier(table,number):
    for i in range(1,11):
        if table[i- 1] != number * i:
            return i - 1
    return None

# Code_starting_point
if __name__ == '__main__':
    number_input = int(input("Enter a number for multiplication table :- "))
    list = multiplication_table(number_input)
    print(f"The multiplication table of {number_input} is displayed below :- \n {list}")

    ask_for_verify = input("Enter \"y\" for verify the result or enter \"n\" to exit :- ")

    if ask_for_verify == "y":
        print(f"The multiplication table was wrong at number {(verifier(list,number_input))+1}.")
    elif ask_for_verify == "n":
        print("Thanks for using our multiplication table system.")
    else:
        print("Please enter between \"y\" and \"n\".")

















# From CodeWithHarry
# '''
# Python Practice problem 8 (Easy, 10 points)
# Rohan Das Is A Fraud
# Rohan das is a fraud by nature.
# Rohan Das wrote a python function to print a multiplication table of a given number and put one of the values (randomly generated) as wrong.
# Rohan Das did this to fool his classmates and make them commit a mistake in a test. You cannot tolerate this!
# So you decided to use your python skills to counter Rohan’s actions by writing a python program that validates Rohan’s multiplication table.
# Your function should be able to find out the wrong values in Rohan’s table and expose Rohan Das as a fraud.
# Note: Rohan’s function returns a list of numbers like this
# Rohan Das’s Function Input:
# rohanMultiplication(6)
# Rohan’s function returns this output:
# [6, 12, 18, 26, …., 60]
# You have to write a function isCorrect(table, number) and return the index where rohan’s function is wrong and print it to the screen! If the table is correct, your function returns None.
# '''
# import random
#
#
# def rohanMultiplication(number):
#     wrong = random.randint(0, 9)
#     table = [i * number for i in range(1, 11)]
#     table[wrong] = table[wrong] + random.randint(0, 10)
#     return table
#
#
# def isCorrect(table, number):
#     for i in range(1, 11):
#         if table[i - 1] != i * number:
#             return i - 1
#
#     return None
#
#
# if __name__ == "__main__":
#     # print(rohanMultiplication(7))
#     number = int(input("Enter a number: "))
#     myTable = rohanMultiplication(number)
#     print(myTable)
#     wrongIndex = isCorrect(myTable, number)
#     print(f"The table is wrong at index {wrongIndex}")
#
#
#
#
#