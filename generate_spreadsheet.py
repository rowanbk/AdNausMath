import calcAN
import itertools

f = open("./output.csv","w")
liferange = range(5,21)
led = "Lions Eye Diamond "
leds = 0
dr = "Dark Ritual "
drs = 0
lp = "Lotus Petal "
lps = 0
it = "Infernal Tutor "
its = 0
floatrange = [0,1,2]
hand = ""
averages = {}
best = 0
for floating in floatrange:
    outlist = ""
    for lps,drs,leds in itertools.product(range(3),repeat=3):
        gone = (led*leds)+(dr*drs)+(lp*lps)+(it*its)
        outlist = ""
        for life in liferange:
            output = calcAN.evaluate("./deck.txt",2,1000,floating,hand,gone,life,1)
            outlist+=str(output)+","
        f.write("'"+str(floating)+str(lps)+str(drs)+str(leds)+","+outlist)
        f.write("\n")
