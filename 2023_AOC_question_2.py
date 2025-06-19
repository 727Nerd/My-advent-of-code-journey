with open("textforadventofcode2.txt") as file:
    games = file.readlines()
#print(games)
    '''
games = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]'''
counter = 0
total = 0
for game in games:
    sentry = True #whether game is possible or not
    counter += 1
    minred = 0
    mingreen = 0
    minblue = 0
    segmentedgame = game.split(";")
    print(segmentedgame)
    for individual in segmentedgame:
        if individual.find(":")>= 0:
            individual = individual[individual.find(":")+2:]
        if individual.find("\n")>= 0:
            individual = individual[:-1]
        individuals = individual.split(",")
        for draw in individuals:
            draw = draw.split(" ")
            print(draw)
            if len(draw) > 2:
                del draw[0]
            draw[0] = int(draw[0])
            if draw[1] == "green":
                if draw[0] > mingreen:
                    mingreen = draw[0]
                
            elif draw[1] == "red":
                if draw[0] > minred:
                    minred = draw[0]
            elif draw[1] == "blue":
                if draw[0] > minblue:
                    minblue = draw[0]
            else:
               print("!!!!!!!!!!!!!!!!!!!!!!!\n"*10)
    total += (minred*mingreen*minblue)
    print(total)
print(total)
        
        
