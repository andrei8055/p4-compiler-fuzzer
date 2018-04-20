from common import common
from annotation import annotation
import random


class action(object):
	annotation = None
	type = 'action'
	name = ''
	parameter_list = []
	expression_list = []

	name_min_length = 1
	name_max_length = 50
	common = common()

	def __init__(self, annotation, name='', parameter_list=[], expression_list=[]):
		self.annotation = annotation
		self.name = name
		self.parameter_list = parameter_list
		self.expression_list = expression_list

	def get_name(self):
		return self.name

	def get_expression_list(self):
		return self.expression_list

	def get_annotation(self):
		return self.annotation

	def get_parameter_list(self):
		return self.parameter_list

	def get_type(self):
		return self.type

	def randomize(self):
		_annotation = annotation()
		_annotation.randomize()
		self.annotation = _annotation
		self.name = self.common.get_random_string(random.randint(self.name_min_length, self.name_max_length), False)
		self.parameter_list = []  #todo randomize parameter list
		self.expression_list = []  #todo randomize expression list

	def generate_code(self):
		code = ''
		if self.annotation is not None:
			code += self.annotation.generate_code()
		code += 'action' + ' '
		code += self.name + '('
		for x in range(0, len(self.parameter_list)):
			code = code + str(self.parameter_list[x].generate_code())
			if x < len(self.parameter_list) - 1:
				code = code + ', '
		code += ') \n'
		code += '{ \n'
		for x in range(0, len(self.expression_list)):
			code = code + str(self.expression_list[x].generate_code())
			code += '\n'
		code += '\n} \n'
		return code

	# actionRef
	#	: optAnnotations name
	#	| optAnnotations name '(' argumentList ')'
	def generate_code_ref(self, parameters):
		code = ''
		if self.annotation is not None:
			code += self.annotation.generate_code() + ' '
		code += self.name
		code += '('
		for x in range(0, len(parameters)):
			code = code + parameters[x]
			if x < len(parameters) - 1:
				code = code + ', '
		code += ')'
		return code