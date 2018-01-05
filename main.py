#!/usr/bin/python
import random
from base_type_generator import base_type_generator
from enum_generator import enum_generator
from header_generator import header_generator
from header_union_generator import header_union_generator
from header_stack_generator import header_stack_generator
from struct_generator import struct_generator

#generate base types
#['void', 'error', 'match', 'bool', 'bit', 'sint', 'varbit', 'int']
base_type_generator = base_type_generator()

void_type = base_type_generator.generate_random_base_type(['void'])
error_type = base_type_generator.generate_random_base_type(['error'])
match_type = base_type_generator.generate_random_base_type(['match'])
bool_type = base_type_generator.generate_random_base_type(['bool'])
bit_type = base_type_generator.generate_random_base_type(['bit'])
sint_type = base_type_generator.generate_random_base_type(['sint'])
varbit_type = base_type_generator.generate_random_base_type(['varbit'])
int = base_type_generator.generate_random_base_type(['int'])

#generate enum
enum_generator = enum_generator()
enum = enum_generator.generate_random()
print enum_generator.generate_code(enum)

#generate headers
header_generator = header_generator()
header_1 = header_generator.generate_random()
print header_generator.generate_code(header_1)

header_2 = header_generator.generate_random()
print header_generator.generate_code(header_2)

#generate headers union
header_union_generator = header_union_generator()
header_union = header_union_generator.generate_random([header_1, header_2])
print header_union_generator.generate_code(header_union)

#generate header stack
header_stack_generator = header_stack_generator()
header_stack = header_stack_generator.generate_random(header_1)
print header_stack_generator.generate_code(header_stack)

header_stack = header_stack_generator.generate_random(header_2)
print header_stack_generator.generate_code(header_stack)

#generate struct
struct_generator = struct_generator()
struct = struct_generator.generate_random([header_1, header_2, error_type, bool_type, bit_type, sint_type, varbit_type,
										   enum, header_stack, header_union])
print struct_generator.generate_code(struct)


#GENERATE PARSERS

#GENERATE INGRESS PROCESSING

#GENERATE EGRESS PROCESSING

#GENERATE DEPARSERS
