from annotation import annotation
from common import common
import random


class enumeration(object):
	annotation = None
	name = ''
	type = 'enum'
	identifiers = []

	name_length = 5
	field_name_length = 5
	field_min_number = 1
	field_max_number = 10

	def __init__(self, annotation=None, name='', identifiers=[]):
		self.annotation = annotation
		self.name = name
		self.identifiers = identifiers

	def get_annotation(self):
		return self.annotation

	def get_name(self):
		return self.name

	def get_identifiers(self):
		return self.identifiers

	def randomize(self):
		common.usedRandomize()
		_annotation = annotation()
		_annotation.randomize()
		self.annotation = _annotation
		self.name = self.generate_name()
		self.identifiers = self.generate_identifiers(random.randint(self.field_min_number, self.field_max_number))

	def generate_code(self):
		return 'enum' + ' ' + self.name + ' ' + '{' + self.generate_fields_code(self.identifiers) + '}\n'

	def generate_code_ref(self):
		code = ''
		if self.annotation is not None:
			code = self.annotation.generate_code() + ' '
		code += self.name
		return code

	def generate_identifiers(self, number):
		identifiers = []
		for x in range(0, number):
			identifiers.append(common.get_random_string(self.field_name_length, True))
		return identifiers

	def generate_name(self):
		code = common.get_random_string(self.name_length, True) + '_enum'
		return code

	def generate_fields_code(self, fields):
		return ', '.join(fields)
