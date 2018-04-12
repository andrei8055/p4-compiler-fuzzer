class state(object):
	name = ''
	body = ''
	#https://p4.org/p4-spec/docs/P4-16-v1.0.0-spec.html#sec-parser-state-stmt
	type = ''

	def __init__(self, name, body, type):
		self.name = name
		self.body = body
		self.type = type

	def get_name(self):
		return self.name

	def get_body(self):
		return self.body

	def get_type(self):
		return self.type
