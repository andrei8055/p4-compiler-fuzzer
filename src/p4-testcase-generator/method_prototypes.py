from method_prototype import method_prototype
from randomizer import randomizer
from common import common


class method_prototypes(object):
	type = 'method_prototypes'
	prototypes_list = []
	min_list_size = 1
	max_list_size = 5

	# methodPrototypes
	# : / *empty * /
	# | methodPrototypes methodPrototype
	# ;

	def __init__(self, prototypes_list=None):
		self.prototypes_list = prototypes_list if prototypes_list is not None else []

	def randomize(self):
		rnd = randomizer.randint(0, 1)
		if rnd == 0:
			self.local_declarations_list = []
		else:
			rndl = randomizer.randint(self.min_list_size, self.max_list_size)
			for x in range(0, rndl):
				_method_prototype = method_prototype()
				_method_prototype.randomize()
				self.prototypes_list.append(_method_prototype)

	def generate_code(self):
		common.usedCodeGenerator(self)
		code = ''
		for method_prototype in self.prototypes_list:
			code += method_prototype.generate_code() + ' ' + "\n"
		return code

