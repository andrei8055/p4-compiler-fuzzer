class prefixed_non_type(object):
	type = 'prefixed_non_type'
	prefix = False
	non_type = None

	def __init__(self, prefix, non_type):
		self.prefix = prefix
		self.non_type = non_type

	def generate_code(self):
		code = ''
		if self.prefix:
			code += '.'
		code += self.non_type.generate_code()
		return code
