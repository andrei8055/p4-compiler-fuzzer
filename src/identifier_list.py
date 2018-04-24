from name import name
import random


class identifier_list(object):
	type = 'identifier_list'
	identifier_list = []
	min_list_size = 1
	max_list_size = 50

	# identifierList
	# : name
	# | identifierList','name
	# ;

	def __init__(self, identifier_list=[]):
		self.identifier_list = identifier_list

	def randomize(self):
		rnd = random.randint(self.min_list_size, self.max_list_size)
		for x in range(0, rnd):
			_name = name()
			_name.randomize()
			self.identifier_list.append(_name)

	def generate_code(self):
		code = ''
		for x in range(0, len(self.identifier_list)):
			code += self.identifier_list[x].generate_code()
			if x < len(self.identifier_list) - 1:
				code = code + ', '
		return code

