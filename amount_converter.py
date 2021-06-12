while(True):
    print("Welcome to amount converter. Write 1 to convert dollar to inr and write 2 to convert inr to dollar")
    amount = int(input())
    if amount==1:
        print("Write the amount")
        value = int(input())
        print(value*72.51, "\n \n")
    elif amount==2:
        print("Write the amount")
        value = int(input())
        print(value*0.014, "\n \n")
    else:
        print("Wrong command! \n \n")