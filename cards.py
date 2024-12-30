import random

# Create a standard 52-card deck
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    return [f"{rank} of {suit}" for suit in suits for rank in ranks]

# Shuffle and draw cards without replacement
def draw_cards(deck, num_cards):
    if num_cards > len(deck):
        print("Not enough cards left in the deck.")
        return []
    drawn_cards = random.sample(deck, num_cards)
    for card in drawn_cards:
        deck.remove(card)
    return drawn_cards

# Initialize the deck
deck = create_deck()
random.shuffle(deck)  # Shuffle the deck initially

# Drawing cards example
while True:
    try:
        num_to_draw = int(input("How many cards would you like to draw? (Enter 0 to quit): "))
        if num_to_draw == 0:
            print("Thanks for playing!")
            break
        drawn_cards = draw_cards(deck, num_to_draw)
        if drawn_cards:
            print("You drew:")
            for card in drawn_cards:
                print(f"  {card}")
            print(f"Cards left in deck: {len(deck)}")
        if len(deck) == 0:
            print("The deck is empty. Game over!")
            break
    except ValueError:
        print("Please enter a valid number.")
