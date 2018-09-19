import random

def wins(cards,hand,remaining,maxLife):
    floating = hand.floating
    currCards = hand.cards.copy()
    floating += currCards.count("Lotus Petal")
    uFloat = 0
    dropped = hand.drop
    if dropped==0:
        for card in cards:
            if cards[card] == 0 and card != "Lotus Petal" and card != "Lions Eye Diamond" and card in currCards:
                dropped = 1
                if card != "Bayou" and card != "Swamp":
                    uFloat = 1
        floating += dropped
    if floating >= 1:
        floating += 2*currCards.count("Dark Ritual")
        floating += (hand.lands-1)*currCards.count("Rain of Filth")
    if floating >= 2:
        floating += 3*currCards.count("Cabal Ritual")
    if floating >= 4 and "Tendrils of Agony" in currCards:
        return 1
    if floating >= 5 and "Infernal Tutor" in currCards and "Dark Petition" in currCards:
        return 1
    if floating >= 2 and "Infernal Tutor" in currCards and "Lions Eye Diamond" in currCards:
        floating += 3*currCards.count("Lions Eye Diamond")
        if floating >= 6:
            return 1
    if floating >= 5 and "Dark Petition" in currCards:
        floating += 3*currCards.count("Lions Eye Diamond")
        if floating >= 6:
            return 1
    if floating + 3*currCards.count("Lions Eye Diamond") >= 7 and "Past in Flames" in currCards:
        return 1
    if "Infernal Tutor" in currCards:
        count = 0
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
                    return 0
        if count <= 0 and floating >= 6:
            hand.life += life
            return 1
    if not "Infernal Tutor" in currCards and not "Dark Petition" in currCards and maxLife - hand.life <= 5 and maxLife > 0 and floating > 4 and ("Ponder" in currCards or "Preordain" in currCards or "Brainstorm" in currCards):
        uFloat += currCards.count("Lotus Petal")
        floating -= uFloat
        visableCards = 0
        locked = 0
        poCount = currCards.count("Ponder")
        prCount = currCards.count("Preordain")
        bsCount = currCards.count("Brainstorm")
        visableCards+=4*min(uFloat,poCount)
        uFloat = max(0,uFloat - poCount)
        if uFloat > 0:
            visableCards += 3*min(uFloat,prCount)
            uFloat = max(0,uFloat - prCount)
        if uFloat > 0 and bsCount > 0:
            visableCards += 3
            uFloat -= 1
            bsCount -= 1
            visableCards += min(uFloat,prCount)
            uFloat = max(0,uFloat - prCount)
        hits = 0
        if floating >= 6:
            hits += remaining.count("Infernal Tutor") + remaining.count("Dark Petition")
        if floating >= 4:
            hits += remaining.count("Tendrils of Agony")
        perCardMiss = float(len(remaining)-hits)/float(len(remaining))
        missPercent = pow(perCardMiss,visableCards)
        nextMissPercent = pow(perCardMiss,visableCards+1)
        killCount = 0
        life = maxLife-hand.life
        for card in remaining:
            if cards[card] >= life:
                killCount += 1
        deathPercent = float(killCount)/float(len(remaining))
        if missPercent < nextMissPercent+deathPercent:
            hitPercent = 1-missPercent
            return hitPercent
        else:
            return 0

    return 0
