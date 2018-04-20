from common import common
from annotation import annotation
import random


class key_element(object):
	annotation = None
	expression = None
	type = 'table_key'
	name = ''

	name_min_length = 1
	name_max_length = 50
	common = common()

	def __init__(self, annotation, name='', expression=None):
		self.annotation = annotation
		self.name = name
		self.expression = expression

	def get_name(self):
		return self.name

	def get_expression(self):
		return self.expression

	def get_annotation(self):
		return self.annotation

	def get_type(self):
		return self.type

	def randomize(self):
		pass

	#  expression ':' name optAnnotations ';'
	def generate_code(self):
		code = ''
		code += self.expression.generate_code() + ' '
		code += ':' + ' '
		code += self.name + ' '
		if self.annotation is not None:
			code += self.annotation.generate_code() + ' '
		code += ';' + ' '
		return code