# Problem-9

# Module
import random

# Function
def name_jumblar(first_name,last_name,name_quantity):
    for i in range(0, name_quantity):
        funny_name = f"{first_name[i]} {last_name[random.randint(0,name_quantity - 1)]}"
        print(funny_name)

# Lists
name_list = []
first_names = []
last_names = []

# Code_starting_point
if __name__ == '__main__':
    print("---Welcome to funny names generator---")
    quantity_of_name = int(input("Enter the quantity of names :- "))

    for i in range(quantity_of_name):
        name_input = input("Enter the name :- ")
        name_list.append(name_input)

    for i in name_list:
        split_names = i.split(" ")
        first_names.append(split_names[0])
        last_names.append(split_names[1])

    name_jumblar(first_names,last_names,quantity_of_name)

# # From_comment_section
# # Python problem 9
# import random
#
# '''
# Author : jayesh kaushik
# program : Jumble words
# Code for : CodeWithHarry(Practice problem 9)
# This function is used for to jumble the words
# '''
#
#
# def jumble_word(first_name, lastt_name, number):
#     for i in range(0, number):
#         # Changing the last name
#         joumbled_name = first_name[i] + " " + lastt_name[random.randint(0, number - 1)]
#         print(joumbled_name)
#
#
#
# if __name__ == "__main__":
#     # Length of the name list
#     number = int(input("Enter the number of names:\n"))
#
#     nameList = []
#     first_name = []
#     lastt_name = []
#
#     # Asking the name of the friends
#     for i in range(1, number + 1):
#         name = input("Enter the name:")
#         # append to the name list
#         nameList.append(name)
#
#     # Spliting the elements of the name list
#     for ele in nameList:
#         split_name = ele.split(" ")
#         # For the first name
#         first_name.append(split_name[0])
#         # For the second name
#         lastt_name.append(split_name[1])
#
#     jumble_word(first_name, lastt_name, number)
