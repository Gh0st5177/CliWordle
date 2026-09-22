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
#--Print-Rules--#
print("0=Not Used, 2=Wrong Place, 1=Correct Place")
#--Pick-A-Word--#
pWords=["green","books","orbit","maple","bacon","maths","angle"]
word=random.choice(pWords).lower()
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
    listedGuess=[]
    for i in guess: listedGuess.append(i)
    for i in listedGuess:
        if i not in listedWord:
            print(0,end="")
        elif i in listedWord and listedWord.index(i)==listedGuess.index(i):
            print(1,end="")
        else:
            print(2,end="")
    if guess==word:
          correct=True
    print()
while guessCount<6 and correct==False:
    Guess()
