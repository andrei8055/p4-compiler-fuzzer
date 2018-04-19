from annotation import annotation
from common import common
from base_type_generator import base_type_generator
from struct_field import struct_field
import random

class header(object):
    annotation = None
    name = ''
    fields = []
    type = 'header'
    base_type = 'header'

    common = common()

    name_length = 15
    field_name_length = 15
    field_min_number = 1
    field_max_number = 15

    base_type_generator = base_type_generator()

    def __init__(self, annotation=None, name='', fields=None):
        self.annotation = annotation
        self.name = name
        self.fields = fields

    def get_annotation(self):
        return self.annotation

    def get_name(self):
        return self.name

    def get_size(self):
        return len(self.fields)

    def get_fields(self):
        return self.fields

    def get_type(self):
        return self.type

    def get_base_type(self):
        return self.base_type

    def randomize(self):
        _annotation = annotation()
        _annotation.randomize()
        self.annotation = _annotation
        self.name = self.generate_name()
        self.fields = self.generate_fields()

    def generate_fields(self):
        varbit_exist = False
        number_of_fields = random.randint(self.field_min_number, self.field_max_number)
        field_list = []
        index = 0
        while index < number_of_fields:
            field = struct_field()
            field.randomize()
            #  only one varbit field allowed per header
            if field.get_type().get_name() == 'varbit':
                if not varbit_exist:
                    field_list.append(field)
                    varbit_exist = True
                    index = index + 1
            else:
                field_list.append(field)
                index = index + 1
        return field_list

    def generate_name(self):
        return self.common.get_random_string(self.name_length, True) + '_h'

    def generate_code(self):
        code = ''
        if self.annotation is not None:
            code = self.annotation.generate_code()
        code += ' ' + 'header' + ' '
        code += self.name
        code += '{'
        for field in self.fields:
            code += field.generate_code() + ' \n'
        code += '}'
        return code