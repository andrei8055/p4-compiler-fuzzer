import random
from annotations import annotations
from common import common


class opt_annotations(object):
	type = 'opt_annotations'
	annotations = None

	# optAnnotations
	# : / *empty * /
	# | annotations
	# ;

	def __init__(self, annotations=None):
		self.annotations = annotations

	def randomize(self):
		common.usedRandomize()
		rnd = random.randint(0, 1)
		if rnd == 0:
			self.annotations = annotations()
			self.annotations.randomize()
		else:
			self.annotations = None

	def generate_code(self):
		if self.annotations is not None:
			return self.annotations.generate_code()
		else:
			return ''
