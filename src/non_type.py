class non_type(object):
	type = 'non_type'
	name = ''

	# nonTypeName
	# : IDENTIFIER
	# | APPLY
	# | KEY
	# | ACTIONS
	# | STATE
	# ;

	def __init__(self, name):
		self.name = name

	def generate_code(self):
		return self.name
