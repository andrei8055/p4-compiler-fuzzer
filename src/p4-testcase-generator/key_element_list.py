from key_element import key_element
from randomizer import randomizer
from common import common


class key_element_list(object):
	element_list = []
	min_list_size = 1
	max_list_size = 2

	type = None
	types = ["empty", "keyElementList"]
	probabilities = [0, 100]

	# keyElementList
	# : / *empty * /
	# | keyElementList keyElement
	# ;

	def __init__(self, element_list=None):
		self.element_list = element_list if element_list is not None else []

	def randomize(self):
		self.type = randomizer.getRandom(self.probabilities)
		if self.type == 0:
			self.element_list = []
		else:
			rndl = randomizer.randint(self.min_list_size, self.max_list_size)
			for x in range(0, rndl):
				_key_element = key_element()
				_key_element.randomize()
				if _key_element.member is not None:
					self.element_list.append(_key_element)

	def generate_code(self):
		common.usedCodeGenerator(self)
		code = ''
		for _key_element in self.element_list:
			code += _key_element.generate_code() + '\n'
		return code

