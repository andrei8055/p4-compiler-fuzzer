from select_case import select_case
from randomizer import randomizer


class select_case_list(object):
	type = 'select_case_list'
	case_list = []
	min_list_size = 1
	max_list_size = 5

	# selectCaseList
	# : / *empty * /
	# | selectCaseList selectCase
	# ;

	def __init__(self, case_list=None):
		self.case_list = case_list if case_list is not None else []

	def randomize(self):
		rnd = randomizer.randint(0, 1)
		if rnd == 0:
			self.case_list = []
		else:
			rndl = randomizer.randint(self.min_list_size, self.max_list_size)
			for x in range(0, rndl):
				_select_case = select_case()
				_select_case.randomize()
				self.case_list.append(_select_case)

	def generate_code(self):
		code = ''
		for select_case in self.case_list:
			code += select_case.generate_code() + ' '
		return code

