import random
import copy


class Card:
	suits = ['s', 'h', 'd', 'c']
	numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
	def __init__(self, suit, number):
		self.suit = suit
		self.number = number

	def to_s(self):
		return f'{self.suit}-{self.number}'


class Deck:
	def __init__(self):
		self.cards = []
		for suit in Card.suits:
			for number in Card.numbers:
				self.cards.append(Card(suit, number))

	def shuffle(self):
		random.shuffle(self.cards)

	def to_s(self):
		return ' '.join(c.to_s() for c in self.cards)


class Game:
	def __init__(self):
		self.deck = Deck()
		self.deck.shuffle()
		self.hand = []

	def try_remove_cards(self, hand):
		has_removed_cards = False
		while len(hand) >= 4:
			if hand[len(hand)-1].number == hand[len(hand)-4].number:
				for x in range(4):
					hand.pop()
				has_removed_cards = True
			elif hand[len(hand)-1].suit == hand[len(hand)-4].suit:
				for x in range(2):
					hand.pop(-2)
				has_removed_cards = True
			else: return has_removed_cards

	def play(self):
		deck = copy.deepcopy(self.deck)
		hand = self.hand
		while len(deck.cards) != 0:
			hand.append(deck.cards.pop())
			if len(hand) < 4:
				continue
			self.try_remove_cards(hand)

		tries = 0
		while tries < 4 and len(hand) >= 4:
			hand.append(hand.pop(0))
			if self.try_remove_cards(hand):
				tries = 0
			else: tries += 1

		return hand


def main():
	results = { 2*x: 0 for x in range(27) }
	for i in range(1000000):
		if i % 100000 == 0:
			print(i / 100000)
		game = Game()
		hand = game.play()
		results[len(hand)] += 1
	print(results)


if __name__ == '__main__':
	main()