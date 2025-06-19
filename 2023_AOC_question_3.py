#text = []
with open("textforadventofcode3.txt") as file:
    text = file.readlines()
    text = [string[:len(string)-1] for string in text]
'''text = ["467..114..",
"...*......",
"..35..633.",
"......#...",
"617*......",
".....+.58.",
"..592.....",
"......755.",
"...$.*....",
".664.598.."]'''
for a in text:
    print(a)
print()
def checkifsymbol(char):
    if char.isalnum():
        return False
    elif char == ".":
        return False
    else:
        return True
#print(text[1])
def checkisnum(x_coord,y_coord):
    answer = []
    directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    for i in directions:
        if y_coord+i[1] < len(text[x_coord+i[0]]):
            if x_coord+i[0] < len(text):
                if text[x_coord+i[0]][y_coord+i[1]].isdigit():
                    ans = text[x_coord+i[0]][y_coord+i[1]]
                    print(ans)
                    #print(text[x_coord+i[0]][y_coord+i[1]])
                    text[x_coord+i[0]] = text[x_coord+i[0]][:y_coord+i[1]] + "/" + text[x_coord+i[0]][y_coord+i[1]+1:]
                    print(text[x_coord+i[0]])
                    sentry = True
                    counter = 1
                    while sentry:
                        if y_coord+i[1] - counter >= 0:
                            if text[x_coord+i[0]][y_coord+i[1]-counter].isdigit(): #check char on the left
                                ans = ans[::-1] + text[x_coord+i[0]][y_coord+i[1]-counter]
                                ans = ans[::-1]
                                print(ans)
                                counter += 1
                                text[x_coord+i[0]] = text[x_coord+i[0]][:y_coord+i[1]-counter+1] + "?" + text[x_coord+i[0]][y_coord+i[1]-counter+2:]
                                print(text[x_coord+i[0]])
                            else:
                                print("Erhrrrrhrhrhrh!")
                                sentry = False
                        else:
                            print("Aaaagh!")
                            sentry = False
                    counter = 1
                    sentry = True
                    while sentry:
                        if y_coord+i[1] + counter < len(text[x_coord+i[0]]): #check char on the right
                            if text[x_coord+i[0]][y_coord+i[1]+counter].isdigit():
                                ans += text[x_coord+i[0]][y_coord+i[1]+counter]
                                print(ans)
                                counter += 1
                                text[x_coord+i[0]] = text[x_coord+i[0]][:y_coord+i[1]+counter-1] + "|" + text[x_coord+i[0]][y_coord+i[1]+counter:]
                                print(text[x_coord+i[0]])
                            else:
                                print("Operational failure!")
                                sentry = False
                        else:
                            print("Big Operational failure!")
                            sentry = False
                    answer.append(int(ans))
                    #print(text[x_coord+i[0]])
                    print(ans)
                    print("----------------------")
    return answer
symbols = []
multiply= []
for i in range(len(text)):
    for j in range(len(text[i])):
        if text[i][j] == "*":
            multiply.append([i,j])
        if checkifsymbol(text[i][j]):
            symbols.append([i,j])
            
total = 0
for coordinate in symbols:
    #print(coordinate)
    for i in checkisnum(coordinate[0], coordinate[1]):
        total += i               
        print(total)
print(total)
