deck = ["32T3K 765",
"T55J5 684",
"KK677 28",
"KTJJT 220",
"QQQJA 483"]
total = 0
order = []
for hand in deck:
    cards,bet = hand.split()
    bet       = int(bet)
    cardlist = []
    for card in cards:
        if card in cardlist:
            cardlist[cardlist.index(card)+1] += 1
        if card not in cardlist:
            cardlist.append(card)
            cardlist.append(1)
    print(cardlist)
    if 5 in cardlist:
        #order.append(cards)
        #order.append(6)
        print(cards,6)
    elif 4 in cardlist:
        #order.append(cards)
        #order.append(6)
        print(cards,5)
        #print(bet*4)
    elif 3 in cardlist:
        if 2 in cardlist:
            #total += bet * 5
            print(cards,4)
            #print(bet)
        else:
            #total += bet * 3
            print(cards,3)
            #print(bet*3)
    elif 2 in cardlist:
        if cardlist.count(2) > 1:
            #total += bet * 2
            print(cards,2)
            #print(bet*2)
        else:
            #print(bet*1)
            print(cards,1)
    else:
        #total += bet * 0
        print(cards,0)
