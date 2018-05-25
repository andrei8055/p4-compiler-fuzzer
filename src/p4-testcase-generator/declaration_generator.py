from expression_generator import expression_generator
from base_type_generator import base_type_generator

class declaration_generator(object):
	expression_generator = expression_generator()
	base_type_generator = base_type_generator()
	action_name_length = 15

	def generate_random_constant(self):
		type = self.base_type_generator.generate_random([])

		return 1

	def generate_constant(self, variable, expression):
		return 'const' + ' ' + variable.get_type() + ' ' + variable.get_type + ' = ' + expression

	def generate_action(self, name, parameters, body):
		code = 'action' + ' ' + name + '('
		for x in range(0, len(parameters)):
			code = code + str(parameters[x])
			if x < len(parameters) - 1:
				code = code + ', '
		code += ') \n'
		code += '{ \n'
		code += body
		code += '\n} \n'
		return code

	def generate_table(self, name, body):
		code = 'table ' + name + ' { \n'
		code += body + '\n'
		code += '} \n'
		return code

	def generate_apply(self, body):
		code = 'apply { \n'
		code += body + '\n'
		code += '} \n'
		return code

	def generate_variable(self):
		return ''