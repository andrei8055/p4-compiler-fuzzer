from parser_state import parser_state
from randomizer import randomizer
from common import common
from scope import scope
from identifier import identifier


class parser_states(object):
	type = 'parser_states'
	parser_states_list = []
	min_list_size = 1
	max_list_size = 5

	# parserStates
	# : parserState
	# | parserStates parserState
	# ;

	def __init__(self, parser_states_list=None):
		self.parser_states_list = parser_states_list if parser_states_list is not None else []

	def randomize(self):
		rnd = randomizer.randint(self.min_list_size, self.max_list_size)
		scope.insert_state("accept", parser_state())
		scope.insert_state("reject", parser_state())
		for x in range(0, rnd):
			_parser_state = parser_state()
			_parser_state.randomize()
			self.parser_states_list.append(_parser_state)
			scope.insert_state(_parser_state.name.generate_code(), _parser_state)
		start_state = parser_state()
		start_state.randomize()
		start_state.name = identifier("start")
		self.parser_states_list.append(start_state)
		scope.insert_state(start_state.name.generate_code(), start_state)


	def generate_code(self):
		common.usedCodeGenerator(self)
		code = ''
		for parser_state in self.parser_states_list:
			code += parser_state.generate_code() + '\n'
		return code

