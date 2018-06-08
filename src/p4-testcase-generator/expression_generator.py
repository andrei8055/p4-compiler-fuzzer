from randomizer import randomizer
from common import common


class expression_generator:
	string_min_length = 1
	string_max_length = 100
	numeric_min_size = 1
	numeric_max_size = 1
	aritmetic_operators = ["+", "-", "*", "/", "%"]
	boolean_operator = ["==", "!=", "&&", "||"]

	def __init__(self):
		pass

	def generate_random(self, type):
		_type = type
		if type in ['bit', 'int']:
			_type = 'arithmetic'
		if type in ['bool']:
			_type = 'bool'
		if type in ['varbit']:
			_type = 'string'
		expression = self.generate_composed_expression(_type)
		expression = self.replace(expression, _type)
		return expression

	def replace(self, expression, type):
		if 'expression' not in expression:
			return expression
		else:
			if randomizer.choice([0, 1]) == 0:
				replace = self.generate_base_expression(type)
				expression = self.nth_repl(expression, 'expression', replace, 1)
				return self.replace(expression, type)
			else:
				replace = self.generate_composed_expression(type)
				expression = self.nth_repl(expression, 'expression', replace, 1)
				return self.replace(expression, type)


	def get_expression_template(self):
		operator = randomizer.choice(self.boolean_operator)
		return '(expression)' + ' ' + operator + ' ' + '(expression)'

	def generate_composed_expression(self, type):
		if type == 'bool':
			operator = randomizer.choice(self.boolean_operator)
			return 'expression' + ' ' + operator + ' ' + 'expression'
		if type == 'string':
			operator = randomizer.choice(["+"])
			return 'expression' + ' ' + operator + ' ' + 'expression'
		if type == 'arithmetic':
			operator = randomizer.choice(self.aritmetic_operators)
			return 'expression' + ' ' + operator + ' ' + 'expression'

	def generate_base_expression(self, type):
		if type == 'bool':
			values = ['true', 'false']
			return randomizer.choice(values)
		if type == 'string':
			return '"' + common.get_random_string(randomizer.randint(self.string_min_length, self.string_max_length), False) + '"'
		if type == 'arithmetic':
			return common.get_random_number(self.numeric_min_size, self.numeric_max_size)

	def nth_repl(self, s, sub, repl, nth):
		find = s.find(sub)
		# if find is not p1 we have found at least one match for the substring
		i = find != -1
		# loop util we find the nth or we find no match
		while find != -1 and i != nth:
			# find + 1 means we start at the last match start index + 1
			find = s.find(sub, find + 1)
			i += 1
		# if i  is equal to nth we found nth matches so replace
		if i == nth:
			return s[:find]+repl+s[find + len(sub):]
		return s

