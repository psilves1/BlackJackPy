from random import randint
from tkinter import *

class Card:


    def __init__(self, num, t=1):
        self.number = num


        if(self.number == 11 or self.number == 12 or self.number == 13):
            self.value = 10
        else:
            self.value = num


        if (t == 1):
            self.type = "Hearts"
        elif (t == 2):
            self.type = "Diamonds"
        elif (t == 3):
            self.type = "Clubs"
        elif (t == 4):
            self.type = "Spades"


    def __str__(self):

        if(self.number == 1):
            return "Ace of " + self.type
        elif(self.number == 11):
            return "Jack of " + self.type
        elif(self.number == 12):
            return "Queen of " + self.type
        elif(self.number == 13):
            return "King of " + self.type
        else:
            return str(self.number) + " of " + self.type


class Deck:

    def __init__(self):

        self.list = []

        x = 1

        while(x<5):
            y = 1
            while(y<14):
                self.list.append(Card(y,x))
                y+=1
            x+=1

    def __getitem__(self, item):
        return self.list[item]

    def __len__(self):
        return len(self.list)


    def dealCard(self):

        return self.list.pop(randint(0, len(deck)-1))


class Player:

    def __init__(self, deck):
        self.hand = []
        self.value = 0

        self.takeCard(deck)
        self.takeCard(deck)

    def printHand(self):
        for c in self.hand:
            print(c)

    def takeCard(self, deck):
        card = deck.dealCard()
        self.hand.append(card)
        self.value += card.value
        return card


    def isOver(self):

        return self.value > 21

    def giveCardsBack(self, deck):

        for c in self.hand:
            deck.list.append(c)

        self.hand = []
        self.value = 0



deck = Deck()
player = Player(deck)
dealer = Player(deck)


#_______________________________________________________________________________________________________________

#GUI Stuff

#master window config
master = Tk()
master.title("Black Jack")
master.geometry("600x400")

playerscards = StringVar(master)

player.printHand()

for c in player.hand:
    playerscards.set(playerscards.get() + str(c) + "\n")

#functions

def hitFunction():
    c = player.takeCard(deck)

    scoreLabel.configure(text="Score: " + str(player.value))


    if(player.isOver()):
        popUpBox("Bust! You lost!")

    playerscards.set(playerscards.get() + str(c) + "\n")
    cardsLabel.configure(text=playerscards.get())

    #print("hitFunction")


def holdFunction():

    print("Player's score: " + str(player.value))
    print("Dealer's score: " + str(dealer.value))

    if(player.value > dealer.value):
        #outcomeLabel.configure(text="You won!")
        popUpBox("You won!")

    elif(player.value < dealer.value):
        #outcomeLabel.configure(text="You lost!")
        popUpBox("You lost!")

    else:
        #outcomeLabel.configure(text="It's a draw!")
        popUpBox("It's a draw!")

    #outcomeLabel.place(x=25, y=65)

    #print("holdFunction")


def yesButtonFunction(popUp, player = player, dealer = dealer):
    player.giveCardsBack(deck)
    dealer.giveCardsBack(deck)
    player.takeCard(deck)
    player.takeCard(deck)
    dealer.takeCard(deck)
    dealer.takeCard(deck)
    playerscards.set("")
    for c in player.hand:
        playerscards.set(playerscards.get() + str(c) + "\n")
    scoreLabel.configure(text="Score: " + str(player.value))
    popUp.destroy()


def popUpBox(message):
    popUp = Toplevel()
    popUp.geometry("220x120")
    popUp.title('')
    outcome = Label(popUp, text=message, font=30)
    outcome.place(x=5, y=5)
    playAgainLabel = Label(popUp, text="Play Again?", font = 30)
    playAgainLabel.place(x=5, y=40)
    yesButton = Button(popUp, text="Yes", command= lambda: yesButtonFunction(popUp))#lambda allows the function to have arguemnts
    yesButton.place(x=60, y = 90)
    noButton = Button(popUp, text="No", command = master.destroy)
    noButton.place(x=100, y=90)


#Buttons

hitButton = Button(master, text="Hit", command=hitFunction)
hitButton.place(x = 25, y = 300)

holdButton = Button(master, text="Hold", command=holdFunction)
holdButton.place(x = 65, y = 300)


#Labels
scoreLabel = Label(master, text="Score: " + str(player.value))
scoreLabel.place(x = 25, y = 25)

cardsLabel = Label(master, textvariable=playerscards)
cardsLabel.place(x = 25, y = 125)

cardsTitleLabel = Label(master, text="Cards:", font="bold")
cardsTitleLabel.place(x = 25, y = 100)

#outcomeLabel = Label(master)

#TODO
#Add dealer label
dealerScoreLabel = Label(master,text= "Dealer's Score: " + str(dealer.value))
#dealerScoreLabel.place(x = 25, y = 50)

#Dealer Logic
while(dealer.value < 15):
    dealer.takeCard(deck)

    if(dealer.value > 21):
        popUpBox("Dealer busted! You win!")



master.mainloop()














