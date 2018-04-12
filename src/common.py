#!/usr/bin/python
import random
import string

class common(object):
	def get_random_string(self, length, first_capital):
		name_length = length
		if first_capital:
			return ''.join(random.choice(string.ascii_lowercase) for _ in range(name_length)).capitalize()
		else:
			return ''.join(random.choice(string.ascii_lowercase) for _ in range(name_length))

	def get_random_number(self, min, max):
		return random.randint(min, max)

	def output(self, code, console, file):
		if console:
			print code
		if file is not None:
			file.write(code)
			file.write('\n')
