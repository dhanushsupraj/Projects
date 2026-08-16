import random

l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']
n= ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
c=["!","@","#","$","%","^","&","*"]

a=int(input("Enter the number of alphabets the password: "))
b=int(input("Enter the number of numbers the password: "))
z=int(input("Enter the number of Characters the password: "))
q=input("DO you want an easy or strong password (EASY)/(STRONG)").lower()

if q=="strong":
    password = []
    for i in range(0, a):
        d = random.randint(0, 51)
        password.append(l[d])

    for k in range(0, b):
        m = random.randint(0, 9)
        password.append(n[m])

    for j in range(0, z):
        o = random.randint(0, 7)
        password.append(c[o])
    # print(password)

    random.shuffle(password)
    # print(password)

    su = ("")
    for n in password:
        su = str(su) + n
    print("Your Password is : ", su)

elif q=="easy":
    password = []
    for i in range(0, a):
        d = random.randint(0, 51)
        password.append(l[d])

    for k in range(0, b):
        m = random.randint(0, 9)
        password.append(n[m])

    for j in range(0, z):
        o = random.randint(0, 7)
        password.append(c[o])
    # print(password)


    # print(password)

    su = ("")
    for n in password:
        su = str(su) + n
    print("Your Password is : ", su)
else:
    print("Invalid Input")


