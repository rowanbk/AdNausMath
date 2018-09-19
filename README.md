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
3. A cantrip line has a higher EV than continueing to flip
4. Passing the turn has a higher EV than continuing to flip
5. Storm count is insufficient
