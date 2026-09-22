import os
import random

pWords=["green","books","orbit","maple","bacon","maths","angle"]
word=random.choice(pWords).lower()
guessCount=0
correct=False

os.system("clear")

print("Cli-Wordle")

def Guess():
    global guessCount
    global correct

    while True:
        guess=input("Guess the word: ")
        if len(guess)!=5:
            print("\033[F\033[2K",end="")
        else:
            break
    if guess.lower()==word:
        print("You Got It!")
        correct=True
    else:
        print("You Don't Got It")
    guessCount+=1

while guessCount<6 and correct==False:
    Guess()
