import numpy as np

file_path = "/mnt/home/tha10/git_repos/advent-of-code-23/input-7-0.txt"

def convert_to_number(card):
    """Convert a card to a number.

    Args:
        card (str): The card to convert

    Returns:
        int: The number of the card
    """

    card_conversion = {"T" : 10, "J" : 1, "Q" : 12, "K" : 13, "A" : 14}
    if card[0] in card_conversion:
        return card_conversion[card[0]]
    else:
        return int(card[0])

def evaluate_hand(hand):
    """Evaluate the type of hand.

    Args:
        hand (ndarray): array of cards representing a hand

    Returns:
        int: cluster to which the hand belongs
    """

    hand_in_func = hand.copy()
    hand_type = {"high_card" : 0, "one_pair" : 1, "two_pairs" : 2, "three_of_a_kind" : 3, "full_house" : 4, "four_of_a_kind" : 5, "five_of_a_kind" : 6}
    unique_cards, count_of_unique_cards = np.unique(hand_in_func[:-1], return_counts=True) # don't include the bid
    
    # if there is a joker (but not all are jokers), determine what it should be before continuing
    if (1 in unique_cards) & (len(unique_cards) > 1):
        hand_in_func = determine_joker(hand_in_func)
        unique_cards, count_of_unique_cards = np.unique(hand_in_func[:-1], return_counts=True)

    number_of_unique_cards = len(unique_cards)

    # case 1 : five of a kind
    if number_of_unique_cards == 1:
        return hand_type["five_of_a_kind"]
    # case 2 : four of a kind or full house
    elif number_of_unique_cards == 2:
        if 4 in count_of_unique_cards:
            return hand_type["four_of_a_kind"]
        else:
            return hand_type["full_house"]
    # case 3 : three of a kind or two pairs
    elif number_of_unique_cards == 3:
        if 3 in count_of_unique_cards:
            return hand_type["three_of_a_kind"]
        else:
            return hand_type["two_pairs"]
    # case 4 : one pair
    elif number_of_unique_cards == 4:
        return hand_type["one_pair"]
    # case 5 : high card
    else:
        return hand_type["high_card"]
    
def determine_joker(hand):
    """Determine what the joker should turn into given the hand.

    Args:
        hand (ndarray): array of cards representing a hand

    Returns:
        ndarray: array of unique cards in the hand with the joker replaced by the best possible card
    """
    # print("Joker detected")
    # print("Hand : ", hand)

    # remove the joker from the hand temporarily
    hand_in_func = hand.copy()
    hand_in_func = np.delete(hand_in_func, np.where(hand_in_func == 1))
    unique_cards, count_of_unique_cards = np.unique(hand_in_func[:-1], return_counts=True)

    largest_count_beside_joker = np.max(count_of_unique_cards)
    card_to_replace_joker = unique_cards[np.where(count_of_unique_cards == largest_count_beside_joker)][0]

    hand[hand == 1] = card_to_replace_joker # replace the joker with the best possible card
    # print("Hand after replacing joker : ", hand)

    return hand
        
            

if __name__ == "__main__":
    with open(file_path, "r") as f:
        input_file = f.read().split("\n")

    # print("Format of the input data : ", input_file[:5])

    # split each line into two lists, one with the cards and one with the bids
    bids = np.empty(len(input_file),dtype=int)
    hands_list = [] # convert to a list first because cards are still strings

    for i, line in enumerate(input_file):
        bids[i] = line.split(" ")[1]
        hands_list.append(list(line.split(" ")[0]))

    # print("Format of the hands in str : ", hands_list[:5])
    # print("Format of the bids : ", bids[:5])

    # convert the cards to integers
    cards_array = np.empty((len(hands_list),len(hands_list[0])+1),dtype=int)

    for i, hand in enumerate(hands_list):
        for j, card in enumerate(hand):
            cards_array[i,j] = convert_to_number(card)
        cards_array[i,-1] = bids[i] # add the bid to the end of the array

    # print("Format of the hands in int : ", cards_array[:5,:])

    # evaluate the hands
    hand_types = np.empty(len(hands_list),dtype=int)
    for i, hand in enumerate(cards_array):
        hand_types[i] = evaluate_hand(hand)

    # print("Format of the hand types : ", hand_types[:5])

    # separate the hands into the different types, and convert back to list for easier sorting
    high_card_hands = cards_array[hand_types == 0].tolist()
    one_pair_hands = cards_array[hand_types == 1].tolist()
    two_pairs_hands = cards_array[hand_types == 2].tolist()
    three_of_a_kind_hands = cards_array[hand_types == 3].tolist()
    full_house_hands = cards_array[hand_types == 4].tolist()
    four_of_a_kind_hands = cards_array[hand_types == 5].tolist()
    five_of_a_kind_hands = cards_array[hand_types == 6].tolist()

    # print("Format of the high card hands : ", high_card_hands[:5])

    # sort the hands
    high_card_hands.sort()
    one_pair_hands.sort()
    two_pairs_hands.sort()
    three_of_a_kind_hands.sort()
    full_house_hands.sort()
    four_of_a_kind_hands.sort()
    five_of_a_kind_hands.sort()

    # print("Format of the high card hands after sort: ", high_card_hands[:5])

    # combine all the hands into one list
    combine_all_hands = []
    combine_all_hands.extend(high_card_hands)
    combine_all_hands.extend(one_pair_hands)
    combine_all_hands.extend(two_pairs_hands)
    combine_all_hands.extend(three_of_a_kind_hands)
    combine_all_hands.extend(full_house_hands)
    combine_all_hands.extend(four_of_a_kind_hands)
    combine_all_hands.extend(five_of_a_kind_hands)

    print("Format of the combined hands : ", combine_all_hands[:5])
    
    # calculate the winnings
    winnings = 0
    for i in range(len(input_file)):
        winnings += (i+1) * combine_all_hands[i][-1]

    print("Winnings : ", winnings)