import random
SU = ["Diamonds","Clubs","Spades","Hearts"]
RA = ["2","3","4","5","6","7","8","9","10","K","Q","J","A"]
class Card:
    def __init__(self, suit, rank):
        if suit not in SU or rank not in RA:
            raise ValueError("Not valid card.")
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self):
        return f"Card({self.suit}, {self.rank})"

class Deck:
    def __init__(self):
        self.cards = []
        for su in SU:
            for ra in RA:
                self.cards.append(Card(su,ra))
        self.len = len(self.cards)
    
    def shuffle(self):
        return random.shuffle(self.cards)
    
    def __len__(self):
        return len(self.cards)
    
    def deal(self):
        if len(self.cards)!=0:
            return self.cards.pop()
        else:
            return None
    def __repr__(self):
        return f"Cards({self.cards})"
    
    def __iter__(self):
        return iter(self.cards)
    
    def __getitem__(self,position):
        return self.cards[position]
    
deck = Deck()
print(deck)
deck.shuffle()
card = deck.deal()
print(card)
print(len(deck))
print(deck[0])
for card in deck:
    print (card) 