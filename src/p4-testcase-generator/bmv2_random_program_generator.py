from struct_type_declaration import struct_type_declaration
from header_type_declaration import header_type_declaration
from extern_declaration import extern_declaration
from extern_variable_creation import extern_variable_creation
from parser_declaration import parser_declaration
from struct_field_list import struct_field_list
from scope import scope
from randomizer import randomizer


class bmv2_random_program_generator(object):

	min_random_structs = 1
	max_random_structs = 10

	min_random_headers = 1
	max_random_headers = 10

	min_random_parsers = 0
	max_random_parsers = 10

	min_random_externs = 1
	max_random_externs = 25

	min_extern_variables = 1
	max_extern_variables = 100

	def __init__(self):
		pass

	def generate(self):
		scope.start_local()
		code = ""
		code += self.output_seed_comment()
		code += self.generate_bmv2_includes()
		code += self.generate_bmv2_structs()
		code += self.generate_random_structs()
		code += self.generate_random_headers()
		code += self.generate_random_externs()
		code += self.generate_extern_variables()
		code += self.generate_bmv2_parser()
		#TODO:continue implement parsers
		#code += self.generate_random_parsers()
		code += self.generate_bmv2_controls()
		self.generate_random_controls()
		code += self.generate_bmv2_init()
		scope.stop_local()
		return code

	def output_seed_comment(self):
		return "//seed: " + str(randomizer.getSeed()) + "\n"

	def generate_bmv2_includes(self):
		# TODO: better
		return "#include <core.p4>\n#include <v1model.p4>\n"


	def generate_bmv2_structs(self):
		headers_t = struct_type_declaration(name="headers_t")
		_struct_field_list = struct_field_list(fromObj=headers_t)
		headers_t.struct_field_list = _struct_field_list
		# TODO: if we randomize headers_t fields we need to write to them all in the parser to avoid warning
		metadata_t = struct_type_declaration(name="metadata_t")
		_struct_field_list2 = struct_field_list(fromObj=metadata_t)
		_struct_field_list2.randomize()
		metadata_t.struct_field_list = _struct_field_list2
		structs = (headers_t, metadata_t)
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

	def generate_bmv2_parser(self):
		# TODO: Implement
		code = "parser ParserImpl(packet_in packet,\nout headers_t hdr,\ninout metadata_t meta,\ninout standard_metadata_t standard_metadata) {\nstate start {\ntransition select() {\n\ndefault: accept;\n}\n}\n}\n\n"
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

	def generate_bmv2_controls(self):
		# TODO: Implement
		code = "control IngressImpl(inout headers_t hdr,\ninout metadata_t meta,\ninout standard_metadata_t standard_metadata) {\napply {\n}\n}\n\n"
		code += "control EgressImpl(inout headers_t hdr,\ninout metadata_t meta,\ninout standard_metadata_t standard_metadata) {\napply {\n\n}\n}\n\n"
		code += "control VerifyChecksumImpl(inout headers_t hdr, inout metadata_t meta) {\napply {\n\n}\n}\n\n"
		code += "control ComputeChecksumImpl(inout headers_t hdr, inout metadata_t meta) {\napply {\n}\n}\n\n"
		code += "control DeparserImpl(packet_out packet, in headers_t hdr) {\napply {\n}\n}\n\n"
		return code

	def generate_random_controls(self):
		pass

	def generate_bmv2_init(self):
		# TODO: implement
		code = "V1Switch(ParserImpl(),\nVerifyChecksumImpl(),\nIngressImpl(),\nEgressImpl(),\nComputeChecksumImpl(),\nDeparserImpl()) main;"
		return code