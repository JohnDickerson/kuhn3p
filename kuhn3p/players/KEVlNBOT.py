import random
from kuhn3p import betting, deck, Player

class KEVlNBOT(Player):
	
	def act(self, state, card):
		if betting.can_bet(state):
			if card >= deck.KING:
				return betting.CHECK
			else:
				return betting.BET
		else:
			if card == deck.ACE:
				return betting.FOLD
			else:
				return betting.CALL

	def __str__(self):
		return 'KEVlNBOT'
