#!/usr/bin/python
import random
from base_type_generator import base_type_generator
from enum_generator import enum_generator
from header_generator import header_generator
from header_union_generator import header_union_generator
from header_stack_generator import header_stack_generator
from struct_generator import struct_generator
from tuple_generator import tuple_generator


# generate base types
# ['void', 'error', 'match', 'bool', 'bit', 'sint', 'varbit', 'int']
base_type_generator = base_type_generator()

void_type = base_type_generator.generate_specific_base_type('void')
error_type = base_type_generator.generate_specific_base_type('error')
match_type = base_type_generator.generate_specific_base_type('match')
bool_type = base_type_generator.generate_specific_base_type('bool')
bit_type = base_type_generator.generate_specific_base_type('bit')
sint_type = base_type_generator.generate_specific_base_type('sint')
varbit_type = base_type_generator.generate_specific_base_type('varbit')
int = base_type_generator.generate_specific_base_type('int')

# generate enum
enum_generator = enum_generator()
enum = enum_generator.generate_random()
print enum_generator.generate_code(enum)

# generate headers
header_generator = header_generator()
header_1 = header_generator.generate_random()
print header_generator.generate_code(header_1)

header_2 = header_generator.generate_random()
print header_generator.generate_code(header_2)

# generate headers union
header_union_generator = header_union_generator()
header_union = header_union_generator.generate_random([header_1, header_2])
print header_union_generator.generate_code(header_union)

# generate header stack
header_stack_generator = header_stack_generator()
header_stack = header_stack_generator.generate_random(header_1, 5)
print header_stack_generator.generate_code(header_stack)

header_stack = header_stack_generator.generate_random(header_2, 5)
print header_stack_generator.generate_code(header_stack)

# generate struct
struct_generator = struct_generator()
struct_1 = struct_generator.generate_random(['error', 'bool', 'bit', 'sint', 'varbit', enum, header_1, header_2,
										   header_union])
print struct_generator.generate_code(struct_1)

# generate struct containing a struct
struct_2 = struct_generator.generate_random(['error', 'bool', 'bit', 'sint', 'varbit', enum, header_1, header_2,
										   header_union, struct_1])
print struct_generator.generate_code(struct_2)

# generate tuple
tuple_generator = tuple_generator()
tuple_1 = tuple_generator.generate_random(['error', 'bool', 'bit', 'sint', 'varbit', enum, header_1, header_2,
										   header_union])
print tuple_generator.generate_code(tuple_1)

# generate tuple containing a struct
tuple_2 = tuple_generator.generate_random(['error', 'bool', 'bit', 'sint', 'varbit', enum, header_1, header_2,
										   header_union, struct_1])
print tuple_generator.generate_code(tuple_2)


# for field in struct_2.get_fields():
# 	print field
# 	if type(field).__name__ is 'derived_type':
# 		print field.get_type() + ' ' + field.get_base_type()
# 		for f in field.get_fields():
# 			if type(f).__name__ is 'derived_type':
# 				print f.get_type()
# 	print ' '


# GENERATE PARSERS

# GENERATE INGRESS PROCESSING

# GENERATE EGRESS PROCESSING

# GENERATE DEPARSERS
