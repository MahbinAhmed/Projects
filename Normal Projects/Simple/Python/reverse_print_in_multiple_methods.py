# Problem-3

# Input_section

# List_section
list = [5,4,3,2,1]

# Method-1
list1 = list[:]
list1.reverse()
print(f"Reverse print using method-1 :- {list1}")

# Method-2
list2 = list[:]
print(f"Reverse print using method-2 :- {list2[::-1]}")

# Method-3
list3 = list[:]
for i in range(len(list3)//2):
    list3[i], list3[-i -1] = list3[-i -1], list3[i]
print(f"Reverse print using method-3 :- {list3}")