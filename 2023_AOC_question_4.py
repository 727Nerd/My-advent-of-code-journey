with open("Q4_Adv_of_code_text_2023.txt") as file:
    cards = file.readlines()
    cards = [card[:-1] for card in cards]
'''cards = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
"Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
"Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]'''
print(cards)
counter = 1
total  = 0
copies = []
outside = 0
for counta in cards:
    copies.append(1)
print(copies)
for card in cards:
    add = False
    comparison = card.split("|")
    print(comparison)
    power = 0
    lottery = comparison[0].split(" ") #FIrst comparison
    lottery.pop()
    print(lottery)
    lucky   = comparison[1].split(" ") #Second comparison
    lucky   = lucky[1:]
    while lucky.count('') > 0:
        del lucky[lucky.index('')]
    print(lucky)
    for i in range(len(lottery)):
        if lottery[i] in lucky:
            print(lottery[i])
            power += 1
            add = True
    #for j in range(copies[counter]):
        #print("m")
    print("--------------")
    for i in range(power):
        print(f"{counter+i} {copies[counter]}")
        #if counter + i < len(cards):
        copies[counter+i] += copies[counter-1]
        #else:
         #   outside += 1
    counter += 1
    if add:
        #print(f"-----------{2**power}---------------")
        total += 2**power
    #else:
     #   break
    print(copies)
    print(f"-------------------------------------")
print(total)
print("-----------------------")
total = 0
for element in copies:
    total += element
    #counter += 1
print(total+outside)
    
