# #Health Management System
#
# def getdate():
#     import datetime
#     dateandtime = datetime.datetime.now()
#     return dateandtime
# #
# def log(a):
#     if a==1:
#         harry_operation_input=int(input("Press 1 for log, 2 for retrive : "))
#         if harry_operation_input==1:
#             operration_type_input = int(input("Press 1 for food, press 2 for exercise : "))
#             if operration_type_input == 1:
#                 with open("HarryFood.txt","a")as op:
#                     print(op.write(str(getdate())+input("Enter your food : ")))
#                 print("Succesfully written.")
#             elif operration_type_input == 2:
#                 with open("HarryExercise.txt","a")as op:
#                     print(op.write(getdate(),"Enter your exercise : "))
#                 print("Succesfully written.")
#         elif harry_operation_input==2:
#             retrive_type_input=int(input("Press 1 for food list, 2 for exercise list : "))
#             if retrive_type_input==1:
#                 with open("HarryFood.txt")as op:
#                     print(op.read())
#             elif retrive_type_input==2:
#                 with open("HarryExercise.txt")as op:
#                     print(op.read())
#
#     elif a==2:
#         rohan_operation_input=int(input("Press 1 for log, 2 for retrive : "))
#         if rohan_operation_input==1:
#             operration_type_input = int(input("Press 1 for food, press 2 for exercise : "))
#             if operration_type_input == 1:
#                 with open("RohanFood.txt","a")as op:
#                     print(op.write( getdate(),"Enter your food : "))
#                 print("Succesfully written.")
#             elif operration_type_input == 2:
#                 with open("RohanExercise.txt","a")as op:
#                     print(op.write(getdate(),"Enter your exercise : "))
#                 print("Succesfully written.")
#         elif rohan_operation_input==2:
#             retrive_type_input=int(input("Press 1 for food list, 2 for exercise list : "))
#             if retrive_type_input==1:
#                 with open("RohanFood.txt")as op:
#                     print(op.read())
#             elif retrive_type_input==2:
#                 with open("RohanExercise.txt")as op:
#                     print(op.read())
#
#     elif a==3:
#         hammad_operation_input=int(input("Press 1 for log, 2 for retrive : "))
#         if hammad_operation_input==1:
#             operration_type_input = int(input("Press 1 for food, press 2 for exercise : "))
#             if operration_type_input == 1:
#                 with open("HammadFood.txt","a")as op:
#                     print(op.write( getdate(),"Enter your food : "))
#                 print("Succesfully written.")
#             elif operration_type_input == 2:
#                 with open("HammadExercise.txt","a")as op:
#                     print(op.write(getdate(),"Enter your exercise : "))
#                 print("Succesfully written.")
#         elif hammad_operation_input==2:
#             retrive_type_input=int(input("Press 1 for food list, 2 for exercise list : "))
#             if retrive_type_input==1:
#                 with open("HammadFood.txt")as op:
#                     print(op.read())
#             elif retrive_type_input==2:
#                 with open("HammadExercise.txt")as op:
#                     print(op.read())
#
# print("Health Mangement System")
# client_input=int(input("Enter 1 for Harry, 2 for Rohan, 3 for Hammad : "))
# log(client_input)


def getdate():
    import datetime
    dateandtime = datetime.datetime.now()
    return dateandtime

def log(a):
    if a==1:
        input_type=int(input("Press 1 for log Food data, press 2 for log Exercise data : "))
        if input_type == 1:
            with open("HarryFood.txt","a") as op:
                op.write(str(getdate())+" : "+ input("Enter your food name : " + "\n" ))
            print("Written Succesfully")
        if input_type == 2:
            with open("HarryExercise.txt","a")as op:
                op.write(str(getdate())+" : "+ input("Enter your exercise name : " + "\n" ))
            print("Witten Succesfully")

    elif a==2:
        input_type=int(input("Press 1 for log Food data, press 2 for log Exercise data : "))
        if input_type == 1:
            with open("RohanFood.txt","a") as op:
                op.write(str(getdate())+" : "+ input("Enter your food name : " + "\n" ))
            print("Written Succesfully")
        if input_type == 2:
            with open("RohanExercise.txt","a")as op:
                op.write(str(getdate())+" : "+ input("Enter your exercise name : " + "\n" ))
            print("Witten Succesfully")

    elif a==3:
        input_type=int(input("Press 1 for log Food data, press 2 for log Exercise data : "))
        if input_type == 1:
            with open("HammadFood.txt","a") as op:
                op.write(str(getdate())+" : "+ input("Enter your food name : " + "\n" ))
            print("Written Succesfully")
        if input_type == 2:
            with open("HammadExercise.txt","a")as op:
                op.write(str(getdate())+" : "+ input("Enter your exercise name : " + "\n" ))
            print("Witten Succesfully")

def retrive(b):
    if b== 1:
        input_type=int(input("Press 1 for retrive Food data, 2 for retrive Exercise data"))
        if input_type==1:
            with open("HarryFood.txt")as op:
                print(op.read())
        if input_type==2:
            with open("HarryExercise.txt")as op:
                print(op.read())

    elif b== 2:
        input_type=int(input("Press 1 for retrive Food data, 2 for retrive Exercise data"))
        if input_type==1:
            with open("RohanFood.txt")as op:
                print(op.read())
        if input_type==2:
            with open("RohanExercise.txt")as op:
                print(op.read())

    elif b == 3:
        input_type=int(input("Press 1 for retrive Food data, 2 for retrive Exercise data"))
        if input_type==1:
            with open("HammadFood.txt")as op:
                print(op.read())
        if input_type==2:
            with open("HammadExercise.txt")as op:
                print(op.read())

print("-----Welcome to Health Management System-----")
choice_input = int(input("Enter 1 for log data or Enter 2 for retrive data : "))

if choice_input == 1:
    client_input=int(input("Press 1 for Harry, 2 for Rohan, 3 for Hammad : "))
    log(client_input)
elif choice_input==2:
    client_input=int(input("Press 1 for Harry, 2 for Rohan, 3 for Hammad : "))
    retrive(client_input)
else:
    print("You entered a wrong number!!!")