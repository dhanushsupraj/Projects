rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

a = input("Pls choose if you want r(rock) p(Paper) s(Scissors): ")
if a == "r":
    print(rock)
elif a=="p":
    print(Paper)
else:
    print(Scissors)
import random
i=random.randint(1,3)
if i==1:
    print("The computer's choice is : ",rock)
elif i==2:
    print("The computer's choice is : ",Paper)
else:
    print("The computer's choice is : ",Scissors)

if i == 2 and a=="r": # c=p d=r
    print("you win")
elif i == 2 and a=="s": # c=p d=s
    print("you win")
elif i == 2 and a=="p": # c=p d=p ---------------------
    print("Tie")

elif i == 1 and a=="s": # c=r d=s
    print("you loose")
elif i == 1 and a=="r": # c=r d=r -------------
    print("Tie")
elif i == 1 and a=="p": # c=r d=p
    print("you win")

elif i == 3 and a == "s":  # c=s d=s ----------
    print("Tie")
elif i == 3 and a == "r":  # c=s d=r
    print("you win")
elif i == 3 and a == "p":  # c=s d=p
    print("you win")


