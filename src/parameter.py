class parameter(object):
	direction = '' #in, out, inout
	type = ''
	name = ''

	def __init__(self, direction='', type='', name=''):
		self.name = name
		self.type = type
		self.direction = direction

	def get_name(self):
		return self.name

	def get_direction(self):
		return self.direction

	def get_type(self):
		return self.type

	def randomize(self):
		pass  #todo make random parameters

	def generate_code(self):
		return self.direction + ' ' + self.type + ' ' + self.name
