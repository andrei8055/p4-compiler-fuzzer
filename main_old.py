#!/usr/bin/python
import sys
from base_type_generator import base_type_generator
from enum_generator import enum_generator
from header_generator import header_generator
from header_union_generator import header_union_generator
from header_stack_generator import header_stack_generator
from struct_generator import struct_generator
from tuple_generator import tuple_generator
from common import common

filename = ""
console = True

if len(sys.argv) > 1:
	filename = sys.argv[1]
	if(sys.argv[2] == ""):
		console = False
	else:
		console = True
else:
	sys.exit("Error! Missing argument 1 - output filename")

# print the program to file
file = open(filename, "w")

common = common()


#generate includes
code = '#include <core.p4> \n'
code = code + '#include <v1model.p4> \n'
common.output(code, console, file)


# generate base types
# ['void', 'error', 'match', 'bool', 'bit', 'varbit', 'int']
base_type_generator = base_type_generator()

void_type = base_type_generator.generate_specific_base_type('void')
error_type = base_type_generator.generate_specific_base_type('error')
match_type = base_type_generator.generate_specific_base_type('match')
bool_type = base_type_generator.generate_specific_base_type('bool')
bit_type = base_type_generator.generate_specific_base_type('bit')
varbit_type = base_type_generator.generate_specific_base_type('varbit')
int = base_type_generator.generate_specific_base_type('int')

# generate enum
enum_generator = enum_generator()
enum = enum_generator.generate_random()

code = enum_generator.generate_code(enum)
common.output(code, console, file)

# generate headers
header_generator = header_generator()
header_1 = header_generator.generate_random()
code = header_generator.generate_code(header_1)
common.output(code, console, file)

# generate header stack
# header_stack_generator = header_stack_generator()
# header_stack = header_stack_generator.generate_random(header_1, 5)
# code = header_stack_generator.generate_code(header_stack)
# common.output(code, console, file)

header_2 = header_generator.generate_random()
code = header_generator.generate_code(header_2)
common.output(code, console, file)

# generate headers union
header_union_generator = header_union_generator()
header_union = header_union_generator.generate_random([header_1, header_2])
code = header_union_generator.generate_code(header_union)
common.output(code, console, file)


# generate struct
struct_generator = struct_generator()
struct_1 = struct_generator.generate_random(['bool', 'bit', 'int', 'varbit', enum, header_1, header_2,
										   header_union])
code = struct_generator.generate_code(struct_1)
common.output(code, console, file)

# generate struct containing a struct
struct_2 = struct_generator.generate_random(['bool', 'bit', 'int', 'varbit', enum, header_1, header_2,
										   header_union, struct_1])
code = struct_generator.generate_code(struct_2)
common.output(code, console, file)

# generate tuple
tuple_generator = tuple_generator()
#tuple_1 = tuple_generator.generate_random(['error', 'bool', 'bit', 'int', 'varbit', enum, header_1, header_2, header_union])
tuple_1 = tuple_generator.generate_random(['bit', 'bit'])
code = tuple_generator.generate_code(tuple_1)
#common.output(code, console, file)

# generate tuple containing a struct
# tuple_2 = tuple_generator.generate_random(['error', 'bool', 'bit', 'int', 'varbit', enum, header_1, header_2, header_union, struct_1])
# code = tuple_generator.generate_code(tuple_2)
# common.output(code, console, file)


# for field in struct_2.get_fields():
# 	print field
# 	if type(field).__name__ is 'derived_type':
# 		print field.get_type() + ' ' + field.get_base_type()
# 		for f in field.get_fields():
# 			if type(f).__name__ is 'derived_type':
# 				print f.get_type()
# 	print ' '

code = ' \n'
code = code + 'header ethernet_t { \n'
code = code + 'bit<48> dst_addr; \n'
code = code + 'bit<48> src_addr; \n'
code = code + 'bit<16> ether_type; \n'
code = code + '} \n'
code = code + 'header ipv4_t { \n'
code = code + 'bit<4>  version; \n'
code = code + 'bit<4>  ihl; \n'
code = code + 'bit<8>  diffserv; \n'
code = code + 'bit<16> len; \n'
code = code + 'bit<16> identification; \n'
code = code + 'bit<3>  flags; \n'
code = code + 'bit<13> frag_offset; \n'
code = code + 'bit<8>  ttl; \n'
code = code + 'bit<8>  protocol; \n'
code = code + 'bit<16> hdr_checksum; \n'
code = code + 'bit<32> src_addr; \n'
code = code + 'bit<32> dst_addr; \n'
code = code + '} \n'
code = code + '@controller_header("packet_in") \n'
code = code + 'header packet_in_header_t { \n'
code = code + 'bit<9> ingress_port; \n'
code = code + '} \n'
code = code + '@controller_header("packet_out") \n'
code = code + 'header packet_out_header_t { \n'
code = code + 'bit<9> egress_port; \n'
code = code + '} \n'
code = code + 'struct headers_t { \n'
code = code + 'ethernet_t ethernet; \n'
code = code + 'ipv4_t ipv4; \n'
code = code + 'packet_out_header_t packet_out; \n'
code = code + 'packet_in_header_t packet_in; \n'
code = code + '} \n'
code = code + 'struct metadata_t { \n'
code = code + '} \n'
code = code + ' \n'
code = code + ' \n'
code = code + ' \n'
code = code + ' \n'
code = code + ' \n'
code = code + ' \n'
code = code + ' \n'

common.output(code, console, file)

# GENERATE PARSERS
code = 'parser ParserImpl(packet_in packet, \n'
code = code + 'out headers_t hdr, \n'
code = code + 'inout metadata_t meta, \n'
code = code + 'inout standard_metadata_t standard_metadata) { \n'
code = code + 'state start { \n'
code = code + 'transition select(standard_metadata.ingress_port) { \n'
code = code + 'default: accept; \n'
code = code + '} \n'
code = code + '} \n'
code = code + ' \n'
code = code + '} \n'

common.output(code, console, file)

code = ''
code = code + 'control VerifyChecksumImpl(inout headers_t hdr, \n'
code = code + 'inout metadata_t meta) { \n'
code = code + 'apply { \n'
code = code + '} \n'
code = code + '} \n'
code = code + 'control ComputeChecksumImpl(inout headers_t hdr, \n'
code = code + 'inout metadata_t meta) { \n'
code = code + 'apply { \n'
code = code + '} \n'
code = code + '} \n'
code = code + 'control IngressImpl(inout headers_t hdr, \n'
code = code + 'inout metadata_t meta, \n'
code = code + 'inout standard_metadata_t  \n'
code = code + 'standard_metadata) { \n'
code = code + 'action _drop () { } \n'
code = code + 'apply { } \n'
code = code + ' } \n'
code = code + 'control EgressImpl(inout headers_t hdr, \n'
code = code + 'inout metadata_t meta, \n'
code = code + 'inout standard_metadata_t \n'
code = code + 'standard_metadata) { \n'
code = code + 'apply{} \n'
code = code + '} \n'
code = code + 'control DeparserImpl(packet_out packet, in  \n'
code = code + 'headers_t hdr) { \n'
code = code + 'apply {} \n'
code = code + '} \n'
code = code + ' \n'
code = code + ' \n'
code = code + ' \n'
code = code + ' \n'


common.output(code, console, file)

# GENERATE INGRESS PROCESSING

# GENERATE EGRESS PROCESSING

# GENERATE DEPARSERS

# GENERATE SWITCH INSTANTIONATION

code = 'V1Switch(ParserImpl(), \n'
code = code + 'VerifyChecksumImpl(), \n'
code = code + 'IngressImpl(), \n'
code = code + 'EgressImpl(), \n'
code = code + 'ComputeChecksumImpl(), \n'
code = code + 'DeparserImpl()) main; \n'
code = code + ' \n'

common.output(code, console, file)