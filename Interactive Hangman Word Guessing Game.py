import random
lives=-1

image = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

name=["pspk","chiru","ravi","mahesh","lokesh"]
word = random.choice(name)

List=[]
for i in word:
	List.append(i)

l=len(word)
print(word)
print("_"*l)

game_over=False
total=[]
while not game_over:
    guess = input("enter your guessed letter : ").lower()
    if guess in word:
        print("The letter you entered Matched 😍with the Word's letter")
        sm = ""
        for k in List:
            if guess == k:
                sm = sm + k
                total.append(k)

            elif k in total:
                sm = sm + k

            else:
                sm += "_"
        print(sm)

        if "_" in sm:
            game_over = False
        else:
            print("You win")
            game_over = True




    else:
        lives= lives + 1
        print(image[lives])
        if lives == 6:
            game_over = True
            print("You lose")
        else:
            print("Sorry Please try again")



print("The letters which you have entered are : ",total)



