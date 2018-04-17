from common import common
from parameter import parameter

class parameter_generator(object):
	common = common()
	
	def generate(self, direction, type, name):
		dir = direction
		if dir not in ["in", "out", "inout"]:
			dir = ''
		return parameter(dir, type, name)

	def generate_code(self, paramter):
		return paramter.direction + ' ' + paramter.type + ' ' + paramter.name

