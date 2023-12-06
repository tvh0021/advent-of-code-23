match_pattern = [4,2,2,1,0,0]

list_result = [1] * len(match_pattern)
list_card = list(range(6))
tally = 0

remaining_cards = list_card.copy()
done_cards = []

element = 0
while remaining_cards != []:
    tally += 1
    print("Considering card ", element)
    for i in range(match_pattern[element]):
        remaining_cards.append(element + 1 + i)
    
    remaining_cards.pop(0)
    done_cards.append(element)
    if element == len(match_pattern) - 1:
        element = remaining_cards[0]
    else:
        element += 1

print("Done cards : ", done_cards)
print("Tally: ", tally)