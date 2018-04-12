from common import common
from parser import parser
from state_generator import state_generator

class parser_generator(object):
	common = common()
	state_generator = state_generator()
	
	def generate(self, name, parameters, states):
		return parser(name, parameters, states)

	def generate_code(self, parser):
		code = 'parser' + ' ' + str(parser.get_name()) + ' ' + '('
		parameters = parser.get_parameters()
		for x in range(0, len(parameters)):
			code = code + str(parameters[x])
			if x < len(parameters) - 1:
				code = code + ', '
		code += ') \n'
		code += '{ \n'
		#code += parser.get_local_elements TODO add
		states = parser.get_states()
		for state in states:
			code = code + self.state_generator.generate_code(state) + '\n'
		code += '} \n'
		return code
