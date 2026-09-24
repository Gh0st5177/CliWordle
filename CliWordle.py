import os
import random

"""
Process:
    Clear Screen
    Pick a word
    Allow player to guess: Check if guess is 5 letters else ask again
    Print the guess and check it changing the color of the text just like the real wordle
    allow players to guess again
    break cycle if the guess is correct or already guessed 6 times
"""
#--Misc-Variables--#
guessCount=0
correct=False
#--Clear-Screen--#
os.system("clear")
#--Pick-A-Word--#
words=open("words.txt","rt").read().splitlines()
word=random.choice(words).lower()
listedWord=[]
for i in word:  listedWord.append(i)
#--Guess-Function--#
def Guess():
    global guessCount
    global word
    global correct
    global listedWord
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
    listedGuess=[]
    for i in guess: listedGuess.append(i)
    for i in listedGuess:
        if i not in listedWord:
            print(f"\033[91m{i}\033[0m",end="")
        elif i in listedWord and listedWord.index(i)==listedGuess.index(i):
            print(f"\033[92m{i}\033[0m",end="")
        else:
            print(f"\033[93m{i}\033[0m",end="")
    if guess==word:
          correct=True
    print()
while guessCount<6 and correct==False:
    Guess()
if guessCount==6:
    print("The word was:",word)
