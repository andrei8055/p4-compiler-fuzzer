class table_key(object):
	key_elements = None
	type = 'table_key'

	name_min_length = 1
	name_max_length = 50

	def __init__(self, key_elements=None):
		self.key_elements = key_elements

	def get_key_elements(self):
		return self.key_elements

	def get_type(self):
		return self.type

	def randomize(self):
		pass

	#  KEY '=' '{' keyElementList '}'
	def generate_code(self):
		code = ''
		code += 'key = { \n'
		for x in range(0, len(self.key_elements)):
			code = code + str(self.key_elements[x].generate_code())
			code += '\n'
		code += '\n} \n'
		return code