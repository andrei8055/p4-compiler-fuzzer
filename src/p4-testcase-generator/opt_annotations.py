from annotations import annotations
from randomizer import randomizer


class opt_annotations(object):
	type = None
	types = ["empty", "annotations"]
	probabilities = [5,5]
	annotations = None

	# optAnnotations
	# : / *empty * /
	# | annotations
	# ;

	def __init__(self, annotations=None):
		self.annotations = annotations

	def randomize(self):
		self.type = randomizer.getRandom(self.probabilities)
		if self.type == 0:
			self.annotations = annotations()
			self.annotations.randomize()
		else:
			self.annotations = None

	def generate_code(self):
		if self.annotations is not None:
			return self.annotations.generate_code()
		else:
			return ''
