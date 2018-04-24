from switch_casse import switch_casse
import random


class switch_casses(object):
	type = 'switch_casses'
	casses = []
	min_list_size = 1
	max_list_size = 50

	# switchCases
	# : / *empty * /
	# | switchCases switchCase
	# ;

	def __init__(self, casses=[]):
		self.casses = casses

	def randomize(self):
		rnd = random.randint(0, 1)
		if rnd == 0:
			self.casses = []
		else:
			rndl = random.randint(self.min_list_size, self.max_list_size)
			for x in range(0, rndl):
				_switch_casse = switch_casse()
				_switch_casse.randomize()
				self.casses.append(_switch_casse)

	def generate_code(self):
		code = ''
		for _switch_casse in self.casses:
			code += _switch_casse.generate_code() + ' '
		return code

