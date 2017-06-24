import itertools
implala=0
tiger=1 #carnivore
meetkat=2 #carnivore
iguana=3
lion=4 #carnivore
flamingo=5 #carnivore, avian
swan=6 # avian
dingo=7 #carnivore
albatross=8 # avian
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
rule10s=set([swan, dingo, flamingo])

def rule10(per):
    for i in range(1, 7):
        if per[i] in rule10s:
            if per[i-1] in carnivores and per[i+1] in carnivores:
                #print [names[x] for x in per], 'True'
                return True
    return False

def rule4(per):
    isrhebok = False
    for i in range(1, 8):
        if per[i] == rhebok:
            isrhebok = True
            if per[i-1] == lion or per[i-1] == albatross:
                return False
    return isrhebok


def rule12(per):
    avians = (albatross, flamingo, swan)
    for i, a1 in enumerate(avians):
        for j, a2 in enumerate(avians):
            if (j > i) and (a1 in per) and (a2 in per) and per.index(a1) > per.index(a2):
                return False
    return True


for per in itertools.permutations(ls, 8): #1m42.203s 19 958 400
    if rule78(per): #0m15.612s 1 209 600
        if rule9(per): #0m11.412s 272 160
            if rule10(per): # 0m10.891s 108560
                if rule4(per) and rule12(per): # 0m10.546s 31 938
                    print([names[x] for x in per])
