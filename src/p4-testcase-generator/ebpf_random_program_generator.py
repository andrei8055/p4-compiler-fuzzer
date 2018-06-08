from struct_type_declaration import struct_type_declaration
from header_type_declaration import header_type_declaration
from extern_declaration import extern_declaration
from extern_variable_creation import extern_variable_creation
from parser_declaration import parser_declaration
from struct_field_list import struct_field_list
from scope import scope
from randomizer import randomizer


class ebpf_random_program_generator(object):

	min_random_structs = 1
	max_random_structs = 25

	min_random_headers = 1
	max_random_headers = 25

	min_random_parsers = 1
	max_random_parsers = 25

	min_random_externs = 1
	max_random_externs = 25

	min_extern_variables = 1
	max_extern_variables = 50

	def __init__(self):
		pass

	def generate(self):
		scope.start_local()
		code = ""
		code += self.output_seed_comment()
		code += self.generate_ebpf_includes()
		code += self.generate_ebpf_structs()
		code += self.generate_random_structs()
		code += self.generate_random_headers()
		code += self.generate_random_externs()
		code += self.generate_extern_variables()
		code += self.generate_ebpf_parser()
		#TODO:continue implement parsers and controls
		#code += self.generate_random_parsers()
		code += self.generate_ebpf_controls()
		self.generate_random_controls()
		code += self.generate_ebpf_init()
		scope.stop_local()
		return code

	def output_seed_comment(self):
		return "//seed: " + str(randomizer.getSeed()) + "\n"

	def generate_ebpf_includes(self):
		return "#include <core.p4>\n#include <ebpf_model.p4>\n"


	def generate_ebpf_structs(self):
		headers_t = struct_type_declaration(name="headers_t")
		_struct_field_list = struct_field_list(fromObj=headers_t)
		headers_t.struct_field_list = _struct_field_list
		structs = [headers_t]
		code = ""
		for struct in structs:
			code += struct.generate_code()
		return code

	def generate_random_structs(self):
		rnd = randomizer.randint(self.min_random_structs, self.max_random_structs)
		struct_type_declarations = []
		for x in range(0, rnd):
			_struct_type_declaration = struct_type_declaration()
			_struct_type_declaration.randomize()
			struct_type_declarations.append(_struct_type_declaration)
		code = ""
		for _struct_type_declaration in struct_type_declarations:
			code += _struct_type_declaration.generate_code()
		return code

	def generate_random_headers(self):
		rnd = randomizer.randint(self.min_random_headers, self.max_random_headers)
		header_type_declarations = []
		for x in range(0, rnd):
			_header_type_declaration = header_type_declaration()
			_header_type_declaration.randomize()
			header_type_declarations.append(_header_type_declaration)
		code = ""
		for _header_type_declaration in header_type_declarations:
			code += _header_type_declaration.generate_code()
		return code

	def generate_random_externs(self):
		rnd = randomizer.randint(self.min_random_externs, self.max_random_externs)
		extern_declarations = []
		for x in range(0, rnd):
			_extern_declaration = extern_declaration()
			_extern_declaration.randomize()
			extern_declarations.append(_extern_declaration)
		code = ""
		for _extern_declaration in extern_declarations:
			code += _extern_declaration.generate_code()
		return code

	def generate_extern_variables(self):
		rnd = randomizer.randint(self.min_extern_variables, self.max_extern_variables)
		extern_variables = []
		for x in range(0, rnd):
			_extern_variable = extern_variable_creation()
			_extern_variable.randomize()
			extern_variables.append(_extern_variable)
		code = ""
		for _extern_variable in extern_variables:
			code += _extern_variable.generate_code()
		return code

	def generate_ebpf_parser(self):
		code = "parser prs(packet_in packet,\nout headers_t hdr) {\nstate start {\ntransition select() {\n\ndefault: accept;\n}\n}\n}\n\n"
		return code

	def generate_random_parsers(self):
		rnd = randomizer.randint(self.min_random_parsers, self.max_random_parsers)
		parser_declarations = []
		for x in range(0, rnd):
			_parser_declaration = parser_declaration()
			_parser_declaration.randomize()
			parser_declarations.append(_parser_declaration)
		code = ""
		for _parser_declaration in parser_declarations:
			code += _parser_declaration.generate_code()
		return code

	def generate_ebpf_controls(self):
		code = "control pipe(inout headers_t headers, out bool pass) {\napply {\n}\n}\n\n"
		return code

	def generate_random_controls(self):
		pass

	def generate_ebpf_init(self):
		code = "ebpfFilter(prs(), pipe()) main;"
		return code