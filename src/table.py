class table(object):
	annotation = None
	type = 'table'
	name = ''
	property_list = []

	name_min_length = 1
	name_max_length = 50

	def __init__(self, annotation, name='', property_list=[]):
		self.annotation = annotation
		self.name = name
		self.property_list = property_list

	def get_name(self):
		return self.name

	def get_property_list(self):
		return self.property_list

	def get_annotation(self):
		return self.annotation

	def get_type(self):
		return self.type

	def randomize(self):
		pass

	def generate_code(self):
		code = ''
		if self.annotation is not None:
			code += self.annotation.generate_code()
		code += 'table' + ' '
		code += self.name + ' '
		code += '{ \n'
		for x in range(0, len(self.property_list)):
			code = code + str(self.property_list[x].generate_code())
			code += '\n'
		code += '\n} \n'
		return code