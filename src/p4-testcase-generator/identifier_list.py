from name import name
from randomizer import randomizer
from common import common


class identifier_list(object):
	type = 'identifier_list'
	identifier_list = []
	min_list_size = 1
	max_list_size = 5

	# identifierList
	# : name
	# | identifierList','name
	# ;

	def __init__(self, identifier_list=None):
		self.identifier_list = identifier_list if identifier_list is not None else []

	def randomize(self):
		rnd = randomizer.randint(self.min_list_size, self.max_list_size)
		for x in range(0, rnd):
			_name = name()
			_name.randomize()
			self.identifier_list.append(_name)

	def generate_code(self):
		common.usedCodeGenerator(self)
		code = ''
		for x in range(0, len(self.identifier_list)):
			code += self.identifier_list[x].generate_code()
			if x < len(self.identifier_list) - 1:
				code = code + ', '
		return code

