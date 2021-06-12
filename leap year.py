# To check that the year is a leap year or not
while(True):
    year = int(input("Write the year: "))

    if year<=0:
        print("\n")
    elif year>0:
        if year%4==0:
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
        print("Invalid year")