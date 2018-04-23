class empty_statement(object):
	type = 'empty_statement'

	def __init__(self):
		pass

	def generate_code(self):
		return ';'
