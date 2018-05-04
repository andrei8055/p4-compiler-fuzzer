from parser_state import parser_state
import random
from common import common


class parser_states(object):
	type = 'parser_states'
	parser_states_list = []
	min_list_size = 1
	max_list_size = 5

	# parserStates
	# : parserState
	# | parserStates parserState
	# ;

	def __init__(self, parser_states_list=[]):
		self.parser_states_list = parser_states_list

	def randomize(self):
		common.usedRandomize()
		rnd = random.randint(self.min_list_size, self.max_list_size)
		for x in range(0, rnd):
			_parser_state = parser_state()
			_parser_state.randomize()
			self.parser_states_list.append(_parser_state)

	def generate_code(self):
		code = ''
		for parser_state in self.parser_states_list:
			code += parser_state.generate_code() + ' '
		return code

