class return_statement(object):
	type = 'return_statement'

	def __init__(self):
		pass

	def generate_code(self):
		return 'return;'
