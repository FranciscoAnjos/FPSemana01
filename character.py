creatures = []

for i in range(3):
    cname = input()
    chp = int(input())
    clvl = int(input())
    creatures.append([cname, (chp, clvl)]) #store HP and level as tuple

print(creatures)

creatures.sort(key=lambda tup: tup[1][1], reverse=True) #sort by level, decreasing

for i in range(len(creatures)):
    print(creatures[i][0]) #print just name
