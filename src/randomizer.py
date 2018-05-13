import random


class randomizer(object):

	seed = None

	@staticmethod
	def setSeed(seed):
		randomizer.seed = seed
		random.seed(seed)

	@staticmethod
	def getRandom(probabilities):
		rnd = random.random() * sum(probabilities)
		for i, w in enumerate(probabilities):
			rnd -= w
			if rnd < 0:
				return i

	@staticmethod
	def randint(min_list_size, max_list_size):
		return random.randint(min_list_size, max_list_size)

	@staticmethod
	def choice(seq):
		return random.choice(seq)


