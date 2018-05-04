import random
from dot_prefix import dot_prefix
from common import common


class prefixed_type(object):
	type = 'prefixed_type'
	prefix = None
	value = None

	# prefixedType
	# : TYPE
	# | dotPrefix TYPE
	# ;

	def __init__(self, prefix=None, value=None):
		self.prefix = prefix
		self.value = value

	def randomize(self):
		# TODO: fix Type literal as it is not a literal (string) but a previously declared type
		common.usedRandomize()
		rnd = random.randint(0, 1)
		if rnd == 0:
			self.prefix = dot_prefix()
			self.value = 'type'
		elif rnd == 1:
			self.prefix = None
			self.value = 'type'
		#  self.value.randomize()

	def generate_code(self):
		if self.prefix is not None:
			return self.prefix.generate_code() + self.value
		else:
			return self.value
