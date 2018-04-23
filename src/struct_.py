from common import common
from annotation import annotation
import random


class struct_(object):

    annotation = None
    name = ''
    fields = []
    type = 'struct'
    base_type = 'struct'

    max_field_name_length = 10

    def __init__(self, annotation=None, name='', fields=[]):
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

    def randomize(self, fields):
        _annotation = annotation()
        _annotation.randomize()
        self.annotation = _annotation
        self.name = self.generate_name()
        self.fields = random.sample(fields, random.randint(0, len(fields)))

    def generate_name(self):
        return common.get_random_string(self.max_field_name_length, True) + '_struct'

    def generate_field_name(self, name):
        return common.get_random_string(self.max_field_name_length, False) + '_' + name

    def generate_code(self):
        code = ''
        if self.annotation is not None:
            code = self.annotation.generate_code() + ' '
        code += 'struct' + ' '
        code += self.name
        code += '{\n'
        for field in self.fields:
            code += '\t' + field.generate_code_ref() + ' ' + self.generate_field_name(field.get_name()) + ';\n'
        code += '}\n'
        return code

    def generate_code_ref(self):
        code = ''
        if self.annotation is not None:
            code = self.annotation.generate_code() + ' '
        code += self.name
        return code