lavafloor = ["#.##..##.",
"..#.##.#.",
"##......#",
"##......#",
"..#.##.#.",
"..##..##.",
"#.#.##.#.",
"",
"#...##..#",
"#....#..#",
"..##..###",
"#####.##.",
"#####.##.",
"..##..###",
"#....#..#"]
sections = [[]]
for lavarow in lavafloor:
    if lavarow == "":
        sections.append([])
    else:
        sections[-1].append(lavarow)
#for i in sections:
 #   print(i)
total = 0
for platz in sections:
    place = []
    mirrorhorpos = -1
    horizon = False
    for i in platz:
        mirrorhorpos += 1
        if place[-1] == i:
            horizon = True
            break
        place.append(i)
    if horizon:
        total += (mirrorhorpos * 100)
    
    vertplatz = []
    for i in range(len(platz[0])):
        vertplatz.append("")
        for j in platz:
            vertplatz[-1] += j[i]
            
    mirrorverpos = -1
    vplace = []
    vertical = False
    for i in vertplatz:
        mirrorverpos += 1
        if vplace[-1] == i:
            vertical = True
            break
        vplace.append(i)
    if vertical:
        total += (mirrorverpos)
print(total)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    