from common import common
from control import control

class control_generator(object):
	common = common()
	
	def generate(self, name, parameters, declarations):
		return control(name, parameters, declarations)

	def generate_code(self, control):
		code = 'control' + ' ' + str(control.get_name()) + ' ' + '('
		parameters = control.get_parameters()
		for x in range(0, len(parameters)):
			code = code + str(parameters[x])
			if x < len(parameters) - 1:
				code = code + ', '
		code += ') \n'
		code += '{ \n'
		#TODO create declaration class and declaration_generator from list of objects
		code += control.get_declarations()
		code += '} \n'
		return code
