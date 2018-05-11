from common import common
from annotation import annotation
from name import name
from parameter_list import parameter_list


class action(object):
	annotation = None
	type = 'action'
	name = ''
	parameter_list = None
	expression_list = []

	name_min_length = 1
	name_max_length = 50

	def __init__(self, annotation, name=None, parameter_list=None, expression_list=[]):
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
		common.usedRandomize()
		_annotation = annotation()
		_annotation.randomize()
		self.annotation = _annotation
		self.name = name()
		self.name.randomize()
		self.parameter_list = parameter_list()
		self.parameter_list.randomize()
		self.expression_list = []  #todo randomize expression list

	def generate_code(self):
		code = ''
		if self.annotation is not None:
			code += self.annotation.generate_code()
		code += 'action' + ' '
		code += self.name.generate_code() + '('
		code += self.parameter_list.generate_code()
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
		code += self.name.generate_code()
		code += '('
		for x in range(0, len(parameters)):
			code = code + parameters[x]
			if x < len(parameters) - 1:
				code = code + ', '
		code += ')'
		return code