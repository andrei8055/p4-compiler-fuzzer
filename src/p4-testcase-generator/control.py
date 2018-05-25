#!/usr/bin/python
class control(object):
	#https://p4.org/p4-spec/docs/P4-16-v1.0.0-spec.html#sec-control
	annotation = None
	type = 'control'
	name = ''
	type_parameters = []
	parameters = []
	local_declarations = []
	apply = None

	def __init__(self, annotation, name, opt_type_parameters, parameters, local_declarations, apply):
		self.annotation = annotation
		self.type = 'parser'
		self.name = name
		self.type_parameters = type_parameters
		self.parameters = parameters
		self.local_declarations = local_declarations
		self.apply = apply

	def get_annotation(self):
		return self.annotation

	def get_type(self):
		return self.type

	def get_name(self):
		return self.name

	def get_type_parameters(self):
		return self.type_parameters

	def get_parameters(self):
		return self.parameters

	def get_local_declarations(self):
		return self.local_declarations

	def get_apply(self):
		return self.apply

	def generate_code(self):
		code = ''
		code += self.annotation.generate_code() + ' '
		code += 'control' + ' '
		code += self.name + ' ' + '('
		parameters = self.parameters
		for x in range(0, len(parameters)):
			code = code + str(parameters[x].generate_code())
			if x < len(parameters) - 1:
				code = code + ', '
		code += ') \n'
		code += '{ \n'
		declarations = self.local_declarations
		for x in range(0, len(declarations)):
			code = code + str(declarations[x].generate_code())
		code += self.apply
		code += '} \n'
		return code

