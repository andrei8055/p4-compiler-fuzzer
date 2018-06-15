from parser_local_element import parser_local_element
from randomizer import randomizer
from common import common


class parser_local_elements(object):
	type = 'parser_local_elements'
	parser_local_elements_list = []
	min_list_size = 1
	max_list_size = 5

	# parserLocalElements
	# : / *empty * /
	# | parserLocalElements parserLocalElement
	# ;

	def __init__(self, parser_local_elements_list=None):
		self.parser_local_elements_list = parser_local_elements_list if parser_local_elements_list is not None else []

	def randomize(self):
		rnd = randomizer.randint(0, 1)
		if rnd == 0:
			self.non_empty_parameter_list = []
		else:
			rndl = randomizer.randint(self.min_list_size, self.max_list_size)
			for x in range(0, rndl):
				_parser_local_element = parser_local_element()
				_parser_local_element.randomize()
				self.parser_local_elements_list.append(_parser_local_element)

	def generate_code(self):
		common.usedCodeGenerator(self)
		code = ''
		for parser_local_element in self.parser_local_elements_list:
			code += parser_local_element.generate_code() + '\n'
		return code

