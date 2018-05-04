from key_element import key_element
import random
from common import common


class key_element_list(object):
	type = 'key_element_list'
	element_list = []
	min_list_size = 1
	max_list_size = 5

	# keyElementList
	# : / *empty * /
	# | keyElementList keyElement
	# ;

	def __init__(self, element_list=[]):
		self.element_list = element_list

	def randomize(self):
		common.usedRandomize()
		rnd = random.randint(0, 1)
		if rnd == 0:
			self.element_list = []
		else:
			rndl = random.randint(self.min_list_size, self.max_list_size)
			for x in range(0, rndl):
				_key_element = key_element()
				_key_element.randomize()
				self.element_list.append(_key_element)

	def generate_code(self):
		code = ''
		for _key_element in self.element_list:
			code += _key_element.generate_code() + ' '
		return code

