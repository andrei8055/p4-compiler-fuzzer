import string
from randomizer import randomizer

class common(object):

	tokens = {}

	@staticmethod
	def get_random_string(length, first_capital):
		name_length = length
		if first_capital:
			return ''.join(randomizer.choice(string.ascii_lowercase) for _ in range(name_length)).capitalize()
		else:
			return ''.join(randomizer.choice(string.ascii_lowercase) for _ in range(name_length))

	@staticmethod
	def get_random_number(min, max):
		return randomizer.randint(min, max)

	@staticmethod
	def output(code, console, file):
		if console:
			print(code)
		if file is not None:
			file.write(code)
			file.write('\n')

	@staticmethod
	def usedRandomize():
		pass

	@staticmethod
	def usedCodeGenerator(fromObj):
		token_name = fromObj.__class__.__name__
		if token_name in common.tokens:
			common.tokens[token_name] += 1
		else:
			common.tokens.update({token_name: 1})

	@staticmethod
	def get_total_tokens():
		total = 0
		for key, value in common.tokens.iteritems():
			total += value
		return total