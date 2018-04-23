from common import common
from myparser import myparser
from state_generator import state_generator


class parser_generator(object):
	common = common()
	state_generator = state_generator()

	def generate(self, name, parameters, constants, variables, states):
		return myparser(name, parameters, constants, variables, states)

	def generate_random(self):
		name = ''
		parameters = []
		constants = []
		variables = []
		states = []
		return self.generate(name, parameters, constants, variables, states)

	def generate_code(self, parser):
		code = 'parser' + ' ' + str(parser.get_name()) + ' ' + '('
		parameters = parser.get_parameters()
		for x in range(0, len(parameters)):
			code = code + (parameters[x].generate_code())
			if x < len(parameters) - 1:
				code = code + ', '
		code += ') \n'
		code += '{ \n'
		constants = parser.get_constants()
		for c in constants:
			code = code + c.generate_code() + '\n'
		states = parser.get_states()
		for state in states:
			code = code + self.state_generator.generate_code(state) + '\n'
		code += '} \n'
		return code
