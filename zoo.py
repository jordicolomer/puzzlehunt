import itertools
implala=0
tiger=1 #carnivore
meetkat=2 #carnivore
iguana=3
lion=4 #carnivore
flamingo=5 #carnivore
swan=6
dingo=7 #carnivore
albatross=8
elk=9
warthog=10
rhebok=11


names = 'implala tiger meetkat iguana lion flamingo swan dingo albatross elk warthog rhebok'.split()
ls=list(range(12))

def rule78(per):
    return \
        (per[3] == 1 and per[1] == 4) or \
        (per[3] == 1 and per[5] == 4) or \
        (per[4] == 1 and per[6] == 4) or \
        (per[4] == 1 and per[2] == 4) or \
        (per[3] == 4 and per[1] == 1) or \
        (per[3] == 4 and per[5] == 1) or \
        (per[4] == 4 and per[6] == 1) or \
        (per[4] == 4 and per[2] == 1)

def rule9(per):
    return per[6-1] == swan or per[6-1] == albatross or per[6-1] == implala

carnivores=set([tiger, meetkat, lion, flamingo, dingo])

def rule10(per):
    return true

for per in itertools.permutations(ls, 8): #1m42.203s 19 958 400
    if rule78(per): #0m15.612s 1 209 600
        if rule9(per): #0m11.412s 272 160
            print [names[x] for x in per]
