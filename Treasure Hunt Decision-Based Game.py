print("Welcome to Treasure Island.")
print("Your mission is to find treasure.")
print("YOu're at the cross road where do you want to go ?")
a = input("Type left or right : ").lower()
if a == "left":
    b= input("you're at the river Bank , do you want to wait or swim ? ").lower()
    if b == "wait":
       c=input("Which door ? y(Yellow) / b(BLUE) / r(RED) ? ").lower()
       if c == "y":
            print("you win! Found the treasure🙌")
       else :
            print("you lose! better luck next time👍")
else:
    print("Game over !")
