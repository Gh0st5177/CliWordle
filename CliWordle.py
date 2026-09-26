#--Imports--#
import os
import random
#--Misc-Variables--#
guessCount=0
correct=False
#--Clear-Screen--#
os.system("clear")
#--Pick-A-Word--#
words=open("words.txt","rt").read().splitlines()
word=random.choice(words).lower()
#--Guess-Function--#
def Guess():
    global guessCount
    global word
    global correct
    #--Creating-The-Guess--#
    while True:
        guess=input()
        if len(guess)!=5:
            print("\033[F\033[2K",end="")
        else:
            break
    guessCount+=1
    #--Processing-The-Guess--#
    print("\033[F",end="")
    for i in range(len(guess)):
        if guess[i] not in word:
            print(f"\033[31m{guess[i]}\033[0m",end="")
        elif guess[i]==word[i]:
            print(f"\033[32m{guess[i]}\033[0m",end="")
        else:
            print(f"\033[33m{guess[i]}\033[0m",end="")
    if guess==word:
          correct=True
    print()
while guessCount<6 and correct==False:
    Guess()
if guessCount==6 and correct==False:
    print("The word was:",word)
