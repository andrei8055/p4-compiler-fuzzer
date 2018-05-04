from non_type_name import non_type_name
from common import common


class expression(object):
	non_type_name = None
	expression = None
	member = None

	def __init__(self, non_type_name=None, expression=None, member=None):
		self.non_type_name = non_type_name
		self.expression = expression
		self.member = member

	def randomize(self):
		common.usedRandomize()
		# TODO: implement
		self.non_type_name = non_type_name()
		self.non_type_name.randomize()

	# expression
	# : INTEGER
	# | TRUE
	# | FALSE
	# | STRING_LITERAL
	# | nonTypeName
	# | '.' nonTypeName
	# | expression '[' expression ']'
	# | expression '[' expression ':' expression ']'
	# | '{' expressionList '}'
	# | '(' expression ')'
	# | '!' expression
	# | '~' expression
	# | '-' expression
	# | '+' expression
	# | typeName '.' member
	# | ERROR '.' member
	# | expression '.' member
	# | expression '*' expression
	# | expression '/' expression
	# | expression '%' expression
	# | expression '+' expression
	# | expression '-' expression
	# | expression SHL expression        // <<
	# | expression '>''>' expression     // check that >> are adjacent
	# | expression LE expression         // <=
	# | expression GE expression         // >=
	# | expression '<' expression
	# | expression '>' expression
	# | expression NE expression         // !=
	# | expression EQ expression         // ==
	# | expression '&' expression
	# | expression '^' expression
	# | expression '|' expression
	# | expression PP expression         // ++
	# | expression AND expression        // &&
	# | expression OR expression         // ||
	# | expression '?' expression ':' expression
	# | expression '<' typeArgumentList '>' '(' argumentList ')'
	# | expression '(' argumentList ')'
	# | typeRef '(' argumentList ')'
	# | '(' typeRef ')' expression
	# ;

	def generate_code(self):
		# TODO: implement correctly
		code = ""
		if self.member is not None and self.expression is not None:
			code += self.expression.generate_code() + "." + self.member.generate_code()
		elif self.non_type_name is not None:
			code += self.non_type_name.generate_code()
		return code