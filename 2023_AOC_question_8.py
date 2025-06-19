with open("Q8_input.txt") as file:
    themap = file.readlines()
'''themap =["LR\n",
"\n",
"11A = (11B, XXX)\n",
"11B = (XXX, 11Z)\n",
"11Z = (11B, XXX)\n",
"22A = (22B, XXX)\n",
"22B = (22C, 22C)\n",
"22C = (22Z, 22Z)\n",
"22Z = (22B, 22B)\n",
"XXX = (XXX, XXX)\n"]'''
themap = [i[:-1] for i in themap]
themap[-1] = "FSC = (QNS, TMF)"
instruction = themap[0]*5000000
#print(instruction)
del themap[0]
print(themap)
themap = sorted(themap)
del themap[0]
#currentelem = "AAA"
parttwo = []
directions = {}
for elem in themap:
    if elem[2] == "A":
        parttwo.append(elem[:3])
        #print(parttwo)
        #print("AAAAAAAAAAA")
for direction in themap:
    directions[direction[:3]] = [direction[7:10],direction[12:15]] #if 3 characters
#print(directions)

counter = 0
'''while currentelem != "ZZZ":
    if instruction[counter] == "R":
        orient = 1
    else:
        orient = 0
    counter += 1
    currentelem = directions[currentelem][orient]'''
all_are_z = False
forparttwoprovis = parttwo
while not all_are_z:
    #print(forparttwoprovis)
    parttwo = forparttwoprovis
    forparttwoprovis = []
    for pos in parttwo:
        if instruction[counter] == "R":
            orient = 1
        else:
            orient = 0
        forparttwoprovis.append(directions[pos][orient])
    counter += 1
    allz = True
    for pos in forparttwoprovis:
        if pos[-1] != "Z":
            allz = False
    if allz:
        all_are_z = True
print(counter)
