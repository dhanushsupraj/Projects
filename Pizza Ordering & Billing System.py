print("Welcome to Pizza HUT!")
bill=0
size=input("What size pizza do you want? S,M or L : ")
S=15
M=20
L=25
if size=="S":
    bill+=S
if size=="M":
    bill+=M
if size=="L":
    bill += L
p=input("Do you want extra peper y(YES) or n(NO): ")
if p=="y":
    if size=="S":
        bill+=2
    else:
        bill+=3
else:
    bill+=0

e=input("DO you want extra Cheese y(YES) or n(NO): ?")
if e=="y":
     bill+=5
else:
     bill+=0

print(f"Your Total Bill to be paid is : ${bill}")