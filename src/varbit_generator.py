from common import common
from varbit import varbit

class varbit_generator(object):
	common = common()

	def generate(self, size):
		return varbit(size)

	def generate_random(self):
		size = 1 #todo randomize
		return self.generate(size)

	def generate_code(self, varbit):
		return varbit.get_name() + '<' + str(varbit.get_size()) + '>'



