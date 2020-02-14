import random 
jackpot=random.randint(1,100)

guess=int(input("Guess Again"))
counter=1

while guess!=jackpot:
                counter+=1
                if guess>jackpot:
                                print("You are close.Guess lower.")
                                guess=int(input("Guess Again"))

                else:
                                print("You are close.Guess higher.")
                                guess=int(input("Guess Again"))

print("Bingo!")
