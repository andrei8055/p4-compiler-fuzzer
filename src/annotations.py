from annotation import annotation
import random
from common import common


class annotations(object):
	annotation_list = []
	min_list_size = 1
	max_list_size = 5

	def __init__(self, annotation_list=[]):
		self.annotation_list = annotation_list

	def get_annotation_list(self):
		return self.annotation_list

	def randomize(self):
		common.usedRandomize()
		rnd = random.randint(self.min_list_size, self.max_list_size)
		for x in range(0, rnd):
			_annotation = annotation()
			_annotation.randomize()
			self.annotation_list.append(_annotation)

	def generate_code(self):
		code = ''
		for _annotation in self.annotation_list:
			code += _annotation.generate_code() + ' '
		return code
