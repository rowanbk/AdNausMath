Args:
-f [int]    Floating Mana               default=0
-l [int]    Life total                  default=0
-r [int]    Number of lands in play     default=1
-t [int]    Number of trials            default=10000
-d [0-1]    Land drop made or not       default=0
-c [String] Cards remaining in hand     default=""
-p [String] Cards played so far         default=""

if a life total is supplied with the -l option the chance of winning between 0
and 1 for this turn will be returned. If the -l option is not specifed, or
specifed as 0, the expected lifeloss required for this Ad Naus to win will be
returned

Scenarios not considered:
1. Tendrils is in the graveyard
2. PiF is in the graveyard
3. Passing the turn has a higher EV than continuing to flip
4. Storm count is insufficient

Example 1.

python3 calcAN.py deck.txt -f 0 -r 3 -d 1 -l 20 -p "Island Ponder Swamp Duress Underground Sea Dark Ritual Lotus Petal Infernal Tutor Lions Eye Diamond"

python3 (my python version)
calcAN.py (program name)
deck.txt (contains decklist)
-f 0  (nothing floating)
-r 3  (3 lands in play, relevant for Rain of Filth)
-d 1  (already played my land for the turn)
-l 20 (20 life remaining)
-p "Island Ponder Swamp Duress Underground Sea Dark Ritual Lotus Petal Infernal Tutor Lions Eye Diamond"
	what I've played so far this game, these cards are removed from the deck for the simulation
-c ""
	no -c option is specifed, since I cast the Ad Nause off LED no cards are left in my hand


Example 2.

python3 calcAN.py deck.txt -f 2 -r 1 -d 1 -l 20 -p "Underground Sea Dark Ritual Dark Ritual Dark Ritual" -c "Lions Eye Diamond"

-f 2  (nothing floating)
-r 1  (1 land in play, relevant for Rain of Filth)
-d 1  (already played my land for the turn)
-l 20 (20 life remaining)
-p "Underground Sea Dark Ritual Dark Ritual Dark Ritual"
	what I've played so far this turn, these cards are removed from the deck for the simulation
-c "Lions Eye Diamond"
	natural Ad Nause allowed me to hold back an LED 
