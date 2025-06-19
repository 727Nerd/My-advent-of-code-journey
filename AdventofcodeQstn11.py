with open("adventofcode11.txt") as file:
    image = file.readlines()
image = [pixel[:-1] for pixel in image]
#image[-1] += "."
image = ["...#......",
".......#..",
"#.........",
"..........",
"......#...",
".#........",
".........#",
"..........",
".......#..",
"#...#....."]
for row in image:
    print(row)
print("----------------")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def expandimage(grid):
    expgrid = [] #expanded grid
    for bar in grid:
        expgrid.append(bar)
        if '#' not in bar:
            for i in range(999999):
                expgrid.append(bar)
    #column now
    fullexpgrid = []
    column = 0
    emptycols = []
    while column < len(expgrid[0]):
        isempty = True
        for line in expgrid:
            if line[column] != '.':
                isempty = False
        if isempty:
            emptycols.append(column)
        column += 1
    for line in expgrid:
        fullexpgrid.append("")
        for newcol in range(len(bar)):
            fullexpgrid[-1] += line[newcol]
            if newcol in emptycols:
                for i in range(999999):
                    fullexpgrid[-1] += line[newcol]
    return fullexpgrid

def findgalaxie(grid):
    to_return = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            #----------------------------------------------------------------------------------------------------------------find it out, append to to_return
            if grid[i][j] == '#':
                to_return.append([j, i]) #x,y coords
    return to_return
def route(startx, starty, destx, desty):
    #dest stands for destination
    lenroute = 0
    if startx >= destx:
        lenroute += startx - destx
    else:
        lenroute += destx - startx
    if starty >= desty:
        lenroute += starty - desty
    else:
        lenroute += desty - starty
    return lenroute
#print(route(5,7,1,10))





expandedimage = expandimage(image)
#for row in expandedimage:
 #   print(row)
print("=======================================================")
galaxies = findgalaxie(expandedimage)
print(galaxies)
memory = []
total = 0
numgalactic = len(galaxies)
for i in range(numgalactic):
    for j in range(i+1,numgalactic):
        home = galaxies[i]
        other = galaxies[j]
        if [i,j] not in memory and [j,i] not in memory:
            memory.append([i,j])
            prevtotal = total
            total += route(home[0], home[1], other[0], other[1])
            #print(total - prevtotal)
    print(numgalactic-i)
            
print(total)
