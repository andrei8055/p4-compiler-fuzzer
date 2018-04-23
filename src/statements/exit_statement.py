class exit_statement(object):
	type = 'exit_statement'

	def __init__(self):
		pass

	def generate_code(self):
		return 'exit;'
