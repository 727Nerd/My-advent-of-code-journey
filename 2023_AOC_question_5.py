with open("textforadventofcode5.txt") as file:
    instructions = file.readlines()
sentry = True
while sentry:
    if instructions.count('\n') >= 1:
        del instructions[instructions.index('\n')]
    else:
        sentry = False
'''instructions = ["seeds: 79 14 55 13\n",
"seed-to-soil map:\n",
"50 98 2\n",
"52 50 48\n",
"soil-to-fertilizer map:\n",
"0 15 37\n",
"37 52 2\n",
"39 0 15\n",
"fertilizer-to-water map:\n",
"49 53 8\n",
"0 11 42\n",
"42 0 7\n",
"57 7 4\n",
"water-to-light map:\n",
"88 18 7\n",
"18 25 70\n",

"light-to-temperature map:\n",
"45 77 23\n",
"81 45 19\n",
"68 64 13\n",
"temperature-to-humidity map:\n",
"0 69 1\n",
"1 0 69\n",
"humidity-to-location map:\n",
"60 56 37\n",
"56 93 4\n"]'''
for i in range(len(instructions)):
    instructions[i] = instructions[i][:-1]
print(instructions)
instr = []
for elem in instructions:
    print(elem)
    if not elem[0].isdigit():
        instr.append("")
    else:
        #print(elem)
        instr[-1] += elem + " "
        #print(instr[-1])
for i in instr:
    print(i)
#total = 0
minloc = 100000000000000000000000000000000000

#forparttwo = []
#counter = 0
mmmm = instructions[0].split()
del mmmm[0]
mmmm = [int(x) for x in mmmm]
'''while counter < len(mmmm):
    for i in range(int(mmmm[counter+1])):
        forparttwo.append(str(i+int(mmmm[counter])))
    counter += 2
print(forparttwo)'''
#for element in instructions[0].split(" "):
counter = 0
while counter < len(mmmm):
    for i in range(mmmm[counter+1]):
        seed = mmmm[counter]+i
        #print(f"Seed - {seed}")
        for j in range(1,8):
            items = instr[j].split(" ")
            #items = items.pop()
            #print(items)
            #items = items[::-1]
            #items.pop()
            #items.pop()
            #items = items[::-1]
            #print(items)
            for i in range(int(len(items)/3)):
                if int(items[3*i+1]) <= seed and int(items[3*i+2])+int(items[3*i+1]) >= seed:
                    seed += int(items[3*i])-int(items[3*i+1])
                    #print(seed)
                    break
        if seed < minloc:
            minloc = seed
    counter += 2
    print("-")
print("--------------------")
print(minloc)

'''ferts = instructions[2].split()
    ferts = ferts[::-1]
    ferts.pop()
    ferts = ferts[::-1]
    for i in range(len(soils)):
        if int(ferts[3*i+1]) <= seed and int(ferts[3*i])+int(ferts[3*i+1]) >= seed:
            seed += ferts[3*i-2]+ferts[3*i+1]

    waters = instructions[3].split()
    waters = waters[::-1]
    waters.pop()
    waters = waters[::-1]
    for i in range(len(waters)):
        if int(waters[3*i+1]) <= seed and int(waters[3*i])+int(waters[3*i+1]) >= seed:
            seed += waters[3*i-2]+waters[3*i+1]

    lights = instructions[4].split()
    lights = lights[::-1]
    lights.pop()
    lights = lights[::-1]
    for i in range(len(soils)):
        if int(lights[3*i+1]) <= seed and int(lights[3*i])+int(lights[3*i+1]) >= seed:
            seed += lights[3*i-2]+lights[3*i+1]

    temps = instructions[2].split()
    temps = temps[::-1]
    temps.pop()
    temps = temps[::-1]
    for i in range(len(temps)):
        if int(temps[3*i+1]) <= seed and int(temps[3*i])+int(temps[3*i+1]) >= seed:
            seed += soils[3*i-2]+soils[3*i+1]
    
    hum
    loc'''
    
#print(total, len(instructions[0].split(" ")))
