from common import common

class tuple(object):
	max_field_name_length = 10

	annotation = None
	name = ''
	fields = []
	values = []
	type = 'tuple'
	base_type = 'tuple'

	def __init__(self, annotation=None, name='', fields=None, values=None):
		self.annotation = annotation
		self.name = name
		self.fields = fields if fields is not None else []
		self.values = values if values is not None else []

	def get_annotation(self):
		return self.annotation

	def get_name(self):
		return self.name

	def get_size(self):
		return len(self.fields)

	def get_fields(self):
		return self.fields

	def get_values(self):
		return self.values

	def get_type(self):
		return self.type

	def get_base_type(self):
		return self.base_type

	def randomize(self, field_types):
		common.usedRandomize()
		pass


	def generate_field_name(self, name):
		return common.get_random_string(self.max_field_name_length, False) + '_' + name

	def generate_code(self):
		code = ''
		if self.annotation is not None:
			code = self.annotation.generate_code() + ' '
		code += 'tuple' + ' '
		code += '<'
		for x in range(0, len(self.fields)):
			code = code + str(self.fields[x].generate_code_ref())
			if x < len(self.fields) - 1:
				code = code + ', '
		code += '>'
		code += ' '
		code += self.name
		code += ' = '
		code += '{'
		for x in range(0, len(self.values)):
			code = code + str(self.values[x])
			if x < len(self.fields) - 1:
				code = code + ', '
		code += '};'
		return code

