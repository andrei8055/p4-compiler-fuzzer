class state(object):
	name = ''
	body = ''
	#https://p4.org/p4-spec/docs/P4-16-v1.0.0-spec.html#sec-parser-state-stmt
	type = ''

	def __init__(self, name, transitions, type):
		self.name = name
		self.transitions = transitions
		self.type = type

	def get_name(self):
		return self.name

	def get_transitions(self):
		return self.transitions

	def get_type(self):
		return self.type
