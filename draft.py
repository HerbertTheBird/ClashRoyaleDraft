cards = []
with open("cards.txt", "r") as file:
    for line in file:
        cards.append(line.strip())
synergy = [[0] * len(cards) for _ in range(len(cards))]
counter = [[0] * len(cards) for _ in range(len(cards))]
usage = [0]*len(cards)

with open("synergy.csv", "r") as file:
    next(file)
    c = 0
    for line in file:
        arr = line.split(",")
        for i in range(1, len(cards)+1):
            synergy[c][i-1] = float(arr[i])
        c+=1
with open("counter.csv", "r") as file:
    next(file)
    c = 0
    for line in file:
        arr = line.split(",")
        for i in range(1, len(cards)+1):
            counter[c][i-1] = float(arr[i])
        c+=1
with open("popularity.csv", "r") as file:
    next(file)
    arr = next(file).split(",")
    for i in range(0, len(cards)):
        usage[i] = float(arr[i])

start = input("do you start\n")
them = []
us = []
turn = start == "yes"
order = [True, False, False, True, True, False, False, True, True, False, False, True, True, False, True, False]
def score(card):
    syn_score = 0
    for i in us:
        syn_score += synergy[card][i]
    counter_score = 0
    for i in them:
        counter_score += counter[card][i]
    if card == 79:
        print(syn_score, counter_score)
    return (syn_score + counter_score)**2+usage[card]/2
for round in order:
    if turn == order:
        scores = []
        for i in range(len(cards)):
            if i in us or i in them:
                continue
            scores.append((i, score(i)))
        scores.sort(key=lambda x: x[1], reverse=True)
        for i in range(10):
            print(cards[scores[i][0]], scores[i][1])
        while True:
            card = input("what did you pick\n").replace(" ", "").replace(".", "").lower()
            found = False
            for i, c in enumerate(cards):
                if c.replace(" ", "").replace(".", "").lower() == card:
                    us.append(i)
                    found = True
                    break
            if found:
                break
    else:
        while True:
            card = input("what did they pick\n").replace(" ", "").replace(".", "").lower()
            found = False
            for i, c in enumerate(cards):
                if c.replace(" ", "").replace(".", "").lower() == card:
                    them.append(i)
                    found = True
                    break
            if found:
                break
    turn = not turn

