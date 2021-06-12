i = 0
while(i<45):
    print("Welcome to my calculator")
    print("Write 's' for sum, 'd' for difference, 'm' for multiplication and 'div' for division")
    op = input()

    # print("Write your first number")
    n1 = input("Write your first number: " )

    # print("Write your second number")
    n2 = input("Write your second number: ")

    if op=="s":
        print("The answer is", int(n1) + int(n2))
        print("")

    if op=="d":
        print("The answer is", int(n1) - int(n2))
        print("")

    if op=="m":
        print("The answer is", int(n1) * int(n2))
        print("")

    if op=="div":
        print("The answer is", int(n1) / int(n2))
        print("")