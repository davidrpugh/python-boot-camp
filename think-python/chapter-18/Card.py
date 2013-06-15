import random

class Card(object):
    """Represents a standard playing card with the following class attributes:
    
        suit_names: (list) List containing the four suits as strings. This list 
                    implies the following mapping between suits and integers:
                        
                        Mapping from suits to integers:
        
                            Spades   = 3
                            Hearts   = 2
                            Diamonds = 1
                            Clubs    = 0
        
        rank_names: (list) List containing the standard ranking of cards.
            
    """
    
    # Variables defined here are called class attributes.
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
                  'Jack', 'Queen', 'King']
                  
    def __init__(self, suit=0, rank=2):
        """Initializes a Card object with the following instance sttributes:
            
            suit: (int)
            rank: (int)
            
        """
        # These are instance attributes.
        self.suit = suit
        self.rank = rank
                           
    def __str__(self):
        string = '%s of %s' % (Card.rank_names[self.rank], 
                               Card.suit_names[self.suit])
        return string
        
    def __cmp__(self, other):
        """Allows us to use relational operators to compare Card objects."""
        t1 = (self.suit, self.rank)
        t2 = (other.suit, other.rank)
        
        return cmp(t1, t2) 
    
class Deck(object):
    
    def __init__(self):
        """Initializes a Deck of cards with the following attributes:
        
           cards: (list) A list of card objects.
           
        """
        self.cards = []
        
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card) 
                
    def __str__(self):
        """print method for a Deck object."""
        res = []
        for card in self.cards:
            res.append(str(card))
            
        return '\n'.join(res)
        
    def pop_card(self):
        """Deals a card from the bottom of the deck."""
        return self.cards.pop()
    
    def add_card(self, card):
        """Adds a card to the deck."""
        self.cards.append(card)
        
    def shuffle(self):
        """Shuffles the deck of cards."""
        random.shuffle(self.cards)  
        
    # solution to exercise 2
    def sort(self):
        """Sorts the deck of cards."""
        self.cards.sort() 
    
    def move_cards(self, hand, num):
        """Moves some number of cards from the deck to a hand."""
        for i in range(num):
            hand.add_card(self.pop_card())
            
    def deal_hands(self,num_hands, num_cards):
        """Takes two parameters, the number of hands and the number of cards per
        hand, and that creates new Hand objects, deals the appropriate number of
        cards per hand, and returns a list of Hand objects.
        
        """
        # creates a list of Hand objects
        hands = [Hand() for i in range(num_hands)]
        
        # deals the hands
        for hand in hands:
            self.move_cards(hand, num_cards)
            
        return hands       
            
class Hand(Deck):
    """Represents a hand of playing cards."""
    
    def __init__(self, label=''):
        """Initializes a hand object."""
        self.cards = []
        self.label = label   
        
def find_defining_class(obj, meth_name):
    """takes an object and a method name (as a string) and returns the class 
    that provides the definition of the method.
    
    """
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty