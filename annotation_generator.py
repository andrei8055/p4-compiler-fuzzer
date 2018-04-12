from common import common
from base_type import base_type

class annotation_generator(object):
	common = common()
	
	def generate(self, name, value):
		return base_type(name, 0, value)

	def generate_code(self, annotation):
		return '@' + str(annotation.get_name()) + '("' + str(annotation.get_type()) + '")'
