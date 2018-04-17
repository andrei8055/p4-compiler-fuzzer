from common import common
from parser import parser
from src.parameter_generator import parameter_generator
from state_generator import state_generator
from src.constant_generator import constant_generator

class parser_generator(object):
	common = common()
	state_generator = state_generator()
	parameter_generator = parameter_generator()
	constant_generator = constant_generator()

	def generate(self, name, parameters, constants, variables, states):
		return parser(name, parameters, constants, variables, states)

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
			code = code + self.parameter_generator.generate_code(parameters[x])
			if x < len(parameters) - 1:
				code = code + ', '
		code += ') \n'
		code += '{ \n'
		constants = parser.get_constants()
		for constant in constants:
			code = code + self.constant_generator.generate_code(constant) + '\n'
		states = parser.get_states()
		for state in states:
			code = code + self.state_generator.generate_code(state) + '\n'
		code += '} \n'
		return code
