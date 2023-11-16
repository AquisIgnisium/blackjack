#Written By Charan Annangudi
import os
import random
pCards = [2,3,4,5,6,7,8,9,"King","Queen","Jack","Ace"]




def CardGen():
    return random.choice(pCards)

def CardInterpret(x):
    for i in pCards:
        if i == 2 or i == 3 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8 or i == 9:
            print(i)
        elif x == "King" or x == "Queen" or x == "Jack":
            return 10
        else:
            return 0

            


def BotMove(deck, viewCard):
    val = 0
    aceCount = 0
    for i in deck:
        x = CardInterpret(i)
        if x != 0:
            val += x
        else:
            aceCount += 1
    if val + (aceCount*11) > 17:
        return "Stand"
    else:
        return "Hit"
    

def Main():
    print("Welcome to Blackjack (Singleplayer)")
    print("Please enter your name")
    name = input(">>")
    print("Here we go!")
    Game(name, 12)

def Game(name, ace):
    p1 = []
    p1.append(CardGen())
    p1.append(CardGen())
    bot = []
    bot.append(CardGen())
    bot.append(CardGen())
    os.system("cls")
    while True:
        print("Your Cards are", p1)
        print("Their open card is", bot[0])
        print("Make your decision! (Hit or Stand)")
        choice1 = input()
        userD = False
        if choice1 == "Hit":
            p1.append(CardGen())
            print("Your new hand is:",p1)
        elif choice1 == "Stand":
            print("You Stood!")
            userD = True
        botD = False
        if BotMove(bot,p1[0]) == "Hit":
            bot.append(CardGen())
            print("The Bot has decided to Hit")
        else:
            print("The Bot has decided to stand")
            botD = True
        pValue = 0
        pCount = 0
        bValue = 0
        bCount = 0
        for i in p1:
            x = CardInterpret(i)
            if x != 0:
                pValue += CardInterpret(i)
            else:
                pCount += 1
        for i in bot:
            x = CardInterpret(i)
            if x != 0:
                bValue += CardInterpret(i) 
            else:
                bCount += 1
        if pCount > 0:
            print("Would you like your ace to be 1 or 11 (just enter 1 or 11)")
            aceChoice = input(">>")
            if aceChoice == "1":
                pValue =+ 1*pValue
            elif aceChoice == "11":
                pValue =+ 11*pValue
        if bCount > 0:
            if (bCount*11 + bValue > 21):
                bValue += bCount
            else:
                bValue += bCount*11
        if pValue > 21:
            print("Bust! You Lose!")
            input("Press Enter to quit")
        elif pValue == 21 or bValue > 21:
            print("Win! You Won!!")
            input("Press enter to quit")
        else:
            print("Next Round!")
            

        
Main()
