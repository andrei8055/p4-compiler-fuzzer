from common import common
from base_type import base_type

class include_generator(object):
	common = common()
	
	def generate(self, name):
		return base_type(name, 0, "include")

	def generate_code(self, include):
		if include.get_type() == 'include':
			return '#include' + '<' + str(include.get_name()) + '>'
