from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

mycards= [(s,r) for s in SUITE for r in RANKS]

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        print("Creating New Ordered Deck of Cards!")
        self.allcards =[(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("SHUFFLING DECK")
        shuffle(self.allcards)

    def split_in_half(self):
        return(self.allcards[:26], self.allcards[26:])


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return ("Contains {} cards".format(len(self.cards)))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_cards(self):
        return self.cards.pop()


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_cards()
        print("{} has placed: {}".format(self.name,drawn_card))
        print('\n')
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return war_cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards
    def still_has_cards(self):
        """
        Returns True if player still has cards
        """
        return len(self.hand.cards) != 0


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
print("Suite",SUITE)
print("Ranks:", RANKS)

# created new Deck & split in half
d = Deck()
d.shuffle()
half1, half2 = d.split_in_half()

#created Both Players
comp = Player("computer", Hand(half1))
name = input("What is your name player? ")
user = Player(name, Hand(half2))

#Set Round Count
total_rounds = 0
war_count = 0

#lets play
while user.still_has_cards() & comp.still_has_cards():
    total_rounds += 1
    print("It is time for a new round!")
    print("Here are the current standings: ")
    print(user.name + " count: " + str(len(user.hand.cards)))
    print(comp.name + " count: " + str(len(comp.hand.cards)))
    print("Both players play a card!")
    print("\n")

    #cards on Table represented by list
    table_cards = []

    #play cards
    c_card = comp.play_card()
    p_card = user.play_card()

    #Add to table cards
    table_cards.append(c_card)
    table_cards.append(p_card)

    #Check for War!
    # Check for War!
    if c_card[1] == p_card[1]:
        war_count += 1
        print("We have a match, time for war!")
        print("Each player removes 3 cards 'face down' and then one card face up")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        # Play cards
        c_card = comp.play_card()
        p_card = user.play_card()

        # Add to table_cards
        table_cards.append(c_card)
        table_cards.append(p_card)

        # Check to see who had higher rank
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print(user.name + " has the higher card, adding to hand.")
            user.hand.add(table_cards)
        else:
            print(comp.name + " has the higher card, adding to hand.")
            comp.hand.add(table_cards)

    else:
        # Check to see who had higher rank
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print(user.name + " has the higher card, adding to hand.")
            user.hand.add(table_cards)
        else:
            print(comp.name + " has the higher card, adding to hand.")
            comp.hand.add(table_cards)

print("Great Game, it lasted: " + str(total_rounds))
print("A war occured " + str(war_count) + " times.")
