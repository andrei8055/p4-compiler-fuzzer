class statement(object):
	#https://p4.org/p4-spec/docs/P4-16-v1.0.0-spec.html#sec-parser-state-stmt

	annotation = None
	name = ''
	parser_statements = []
	transition_statement = []
	type = 'state'

	def __init__(self, annotation=None, name='', parser_statements=[], transition_statement=[]):
		self.annotation = annotation
		self.name = name
		self.parser_statements = parser_statements
		self.transition_statement = transition_statement

	def get_name(self):
		return self.name

	def get_annotation(self):
		return self.annotation

	def get_parser_statements(self):
		return self.parser_statements

	def get_transition_statement(self):
		return self.transition_statement

	def get_type(self):
		return self.type
