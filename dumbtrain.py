cards = []
with open("cards.txt", "r") as file:
    for line in file:
        cards.append(line.strip())
usage = [0]* len(cards)
synergy = [[0] * len(cards) for _ in range(len(cards))]
counter = [[0] * len(cards) for _ in range(len(cards))]
matchup = [[0] * len(cards) for _ in range(len(cards))]
c = 0
with open("gamesLong.csv", "r") as file:
    next(file)
    for line in file:
        c += 1
        if c % 100000 == 0:
            print(c)
        arr = line.split(",")
        win = arr[17]=="win\n"
        for i in range(1, 9):
            for j in range(9, 17):
                matchup[int(arr[i])][int(arr[j])] += 1
                matchup[int(arr[j])][int(arr[i])] += 1
                if win:
                    counter[int(arr[i])][int(arr[j])] += 1
                else:
                    counter[int(arr[j])][int(arr[i])] += 1
        for i in range(1, 9):
            usage[int(arr[i])]+=1
            for j in range(i+1, 9):
                if win:
                    synergy[int(arr[i])][int(arr[j])] += 1.2
                    synergy[int(arr[j])][int(arr[i])] += 1.2
                else:
                    synergy[int(arr[i])][int(arr[j])] += 0.8
                    synergy[int(arr[j])][int(arr[i])] += 0.8
        for i in range(9, 17):
            usage[int(arr[i])]+=1
            for j in range(i+1, 17):
                if not win:
                    synergy[int(arr[i])][int(arr[j])] += 1.2
                    synergy[int(arr[j])][int(arr[i])] += 1.2
                else:
                    synergy[int(arr[i])][int(arr[j])] += 0.8
                    synergy[int(arr[j])][int(arr[i])] += 0.8
with open("synergy.csv", "w") as file:
    file.write("card,")
    file.write(",".join(cards))
    file.write("\n")
    for i in range(len(cards)):
        file.write(cards[i]+",")
        for j in range(len(cards)):
            synergy[i][j] = round(synergy[i][j]/usage[j], 3)
        file.write(",".join(list(map(str, synergy[i]))) + "\n")
with open("counter.csv", "w") as file:
    file.write("card,")
    file.write(",".join(cards))
    file.write("\n")
    for i in range(len(cards)):
        file.write(cards[i]+",")
        for j in range(len(cards)):
            counter[i][j] = round(counter[i][j]/matchup[i][j], 3)
        file.write(",".join(list(map(str, counter[i]))) + "\n")
with open("popularity.csv", "w") as file:
    file.write(",".join(cards))
    file.write("\n")
    for i in range(len(cards)):
        usage[i] = round(usage[i]/(c*16), 3)
    file.write(",".join(list(map(str, usage))) + "\n")