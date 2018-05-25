from randomizer import randomizer
from prefixed_non_type_name import prefixed_non_type_name
from member import member
from expression import expression

class l_value:
	type = None
	types = ["prefixedNonTypeName", "lValueMemberAccess", "lValueArrayAccess", "lValueArrayRange"]
	probabilities = [3, 2, 3, 2]

	maxDepth = 2
	curDepth = 0

	prefixedNonTypeName = None
	lvalue = None
	member = None
	expression = None
	expression2 = None

	# lvalue
	# 	: prefixedNonTypeName
	# 	| lvalue '.' member
	# 	| lvalue '[' expression ']'
	# 	| lvalue'['expression':'expression']'


	def __init__(self, prefixedNonTypeName=None, lvalue=None, member=None, expression=None, expression2=None):
		self.prefixedNonTypeName = prefixedNonTypeName
		self.lvalue = lvalue
		self.member = member
		self.expression = expression
		self.expression2 = expression2
		pass

	def randomize(self):
		self.__class__.curDepth += 1
		while True:
			self.type = randomizer.getRandom(self.probabilities)
			if self.type == 0:
				self.prefixedNonTypeName = prefixed_non_type_name()
				self.prefixedNonTypeName.randomize()
			elif self.type == 1:
				self.lvalue = l_value()
				self.member = member()
				self.member.randomize()
			elif self.type == 2:
				self.lvalue = l_value()
				self.expression = expression()
				self.expression.randomize()
			elif self.type == 3:
				self.lvalue = l_value()
				self.expression = expression()
				self.expression.randomize()
				self.expression2 = expression()
				self.expression2.randomize()
			if self.__class__.curDepth < self.__class__.maxDepth:
				if self.lvalue is not None:
					self.lvalue.randomize()
				if not self.filter():
					break
			else:
				self.__class__.curDepth -= 1
		self.__class__.curDepth -= 1

	def filter(self):
		return False

	def generate_code(self):
		code = ""
		if self.type == 0:
			code += self.prefixedNonTypeName.generate_code()
		elif self.type == 1:
			code += self.lvalue.generate_code() + "." + self.member.generate_code()
		elif self.type == 2:
			code += self.lvalue.generate_code() + "[" + self.expression.generate_code() + "]"
		elif self.type == 3:
			code += self.lvalue.generate_code() + "[" + self.expression.generate_code() + ":" + self.expression2.generate_code() + "]"

