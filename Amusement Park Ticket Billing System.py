print("welcome to roller coaster !")
name = input("please enter your name: ")
age = int(input("please enter your age: "))
h = int(input("pls enter ur height in cm : "))
if h>120:
    print("Dear",name + " You can proceed!")
    if age<5:
        bill=12
        print("FESS - $ 12")
    elif age<7:
        bill=5
        print("FESS - $ 5")
    elif age<10:
        bill=1
        print("pay 1CR")
    elif age<15:
        bill=10
        print("FESS - $ 10")
    else :
        bill=7
        print("FESS - $ 7")
    p=input("DO you want memories y(YES) or n(NO): ")
    if p == "y":
        print("Your total bill is including PHOTOGRAPHS ($3) : $",bill+3)
    else :
        print("Your total bill is: $",bill)
else :
    print("Dear",name + "     Pls go back to home")