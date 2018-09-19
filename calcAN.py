import re
import random
import argparse

cards = {}

class Deck(object):

    def __init__(self):
        self.decklist = []
        self.deck = []

    def shuffle(self):
        self.deck = self.decklist.copy()
        random.shuffle(self.deck)

    def add(self,count,card,cmc):
        for i in range(int(count)):
            self.deck.append(card)
            self.decklist.append(card)
        cards[card] = int(cmc)

    def remove(self,cards):
        for card in cards:
            self.decklist.remove(card)

    def draw(self):
        return self.deck.pop()

class Hand(object):

    def __init__(self,starting = [],floating = 0,lands=0,drop=1):
        self.start = starting.copy()
        self.cards = []
        self.life = 0
        self.floating = floating
        self.lands = lands
        self.drop = drop

    def wins(self):
        floating = self.floating
        currCards = self.cards.copy()
        floating += currCards.count("Lotus Petal")
        if self.drop==0:
            for card in cards:
                if cards[card] == 0 and card != "Lotus Petal" and card != "Lions Eye Diamond" and card in currCards:
                    floating += 1
                    break
        if floating >= 1:
            floating += 2*currCards.count("Dark Ritual")
            floating += (self.lands-1)*currCards.count("Rain of Filth")
        if floating >= 2:
            floating += 3*currCards.count("Cabal Ritual")
        if floating >= 4 and "Tendrils of Agony" in currCards:
            return True
        if floating >= 5 and "Infernal Tutor" in currCards and "Dark Petition" in currCards:
            return True
        if floating >= 2 and "Infernal Tutor" in currCards and "Lions Eye Diamond" in currCards:
            floating += 3*currCards.count("Lions Eye Diamond")
            if floating >= 6:
                return True
        if floating >= 5 and "Dark Petition" in currCards:
            floating += 3*currCards.count("Lions Eye Diamond")
            if floating >= 6:
                return True
        if floating + 3*currCards.count("Lions Eye Diamond") >= 7 and "Past in Flames" in currCards:
            return True
        if "Infernal Tutor" in currCards:
            count = 0
            dropped = self.drop
            life = 0
            for card in currCards:
                if card == "Duress":
                    floating -= 1
                if card in ["Ponder","Preordain","Brainstorm","Past in Flames"]:
                    count += 1
                if card == "Thoughtseize":
                    count -= 1
                    floating -= 1
                    life += 2
                if card in ["Polluted Delta","Misty Rainforest","Bloodstained Mire","Underground Sea","Volcanic Island","Bayou","Tropical Island","Island","Swamp"]:
                    if dropped == 0:
                        dropped = 1
                    else:
                        return False
            if count <= 0 and floating >= 6:
                self.life += life
                return True


        return False

    def reset(self):
        self.cards = self.start.copy()
        self.life = 0

    def add(self,card):
        self.life += cards[card]
        self.cards.append(card)

def evaluate(inPath,lands,trials,floating,handString,playedString,startingLife,drop):
    f = open(inPath,"r")
    lifetotal = 0
    wins = 0

    deck = Deck()

    for line in f:
        line = line.rstrip('\n')
        parts = line.split()
        deck.add(parts[0],' '.join(parts[1:-1]),parts[-1])

    name = ''
    startingHand = []
    for word in handString.split():
        name+=word
        if name in cards:
            startingHand.append(name)
            name = ''
        else:
            name+=' '
    name = ''
    played = ["Ad Nauseam"]
    for word in playedString.split():
        name+=word
        if name in cards:
            played.append(name)
            name = ''
        else:
            name+=' '

    deck.remove(startingHand)
    deck.remove(played)
    hand = Hand(startingHand,floating,lands,drop)

    for _ in range(trials):
        hand.reset()
        deck.shuffle()
        hand.add(deck.draw())
        while not hand.wins():
            hand.add(deck.draw())
            if startingLife != 0 and hand.life >= startingLife:
                break
        if startingLife == 0:
            lifetotal += hand.life
        elif hand.life < startingLife:
            wins+=1

    lifeAvg = float(lifetotal)/float(trials)
    winPercent = (float(wins)/float(trials))
    if startingLife == 0:
        return lifeAvg
    else:
        return winPercent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    parser.add_argument('-f',help = "[int]    Floating Mana", type=int,default=0)
    parser.add_argument('-l',help = "[int]    Life total",type=int,default=0)
    parser.add_argument('-r',help = "[int]    Number of lands in play", type=int,default=1)
    parser.add_argument('-t',help = "[int]    Number of trials", type=int,default=10000)
    parser.add_argument('-d',help = "[0-1]    Land drop made or not", type=int,default=0)
    parser.add_argument('-c',help = "[String] Cards in hand", default="")
    parser.add_argument('-p',help = "[String] Cards played so far", default="")
    args = parser.parse_args()


    lands = vars(args)['r']
    trials = vars(args)['t']
    drop = vars(args)['d']
    floating = vars(args)['f']
    hand = vars(args)['c']
    played = vars(args)['p']
    startingLife = vars(args)['l']
    f = vars(args)['path']

    print(evaluate(f,lands,trials,floating,hand,played,startingLife,drop))

if __name__ == "__main__":
    main()
