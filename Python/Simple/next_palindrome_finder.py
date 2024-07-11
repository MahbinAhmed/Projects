# Problem-4

# Function_section
def next_palindrome(a):
    a +=1
    while not is_palindrome(a):
        a +=1
    return a

def is_palindrome(a):
    return str(a) == str(a)[::-1]

# List_section
list = []
# Input_section
loop_input = int(input("For how many numbers you want to check:- "))
for i in range(loop_input):
    a = int(input("Enter the number :- "))
    list.append(a)

for i in range(loop_input):
    print(f"The next palindrome for {list[i]} is {next_palindrome(list[i])}")