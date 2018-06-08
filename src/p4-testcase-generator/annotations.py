from annotation import annotation
from randomizer import randomizer
from common import common


class annotations(object):
	annotation_list = []
	min_list_size = 1
	max_list_size = 5

	def __init__(self, annotation_list=None):
		self.annotation_list = annotation_list if annotation_list is not None else []

	def get_annotation_list(self):
		return self.annotation_list

	def randomize(self):
		rnd = randomizer.randint(self.min_list_size, self.max_list_size)
		for x in range(0, rnd):
			_annotation = annotation()
			_annotation.randomize()
			self.annotation_list.append(_annotation)

	def generate_code(self):
		common.usedCodeGenerator(self)
		code = ''
		for _annotation in self.annotation_list:
			code += _annotation.generate_code() + '\n'
		return code
