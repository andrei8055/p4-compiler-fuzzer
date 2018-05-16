from annotation import annotation
from common import common
from randomizer import randomizer


class header_union(object):
    annotation = None
    name = ''
    headers = []
    type = 'header_union'

    name_length = 15
    field_name_length = 15
    field_min_number = 1
    field_max_number = 15

    def __init__(self, annotation=None, name='', headers=None):
        self.annotation = annotation
        self.name = name
        self.headers = headers

    def get_annotation(self):
        return self.annotation

    def get_name(self):
        return self.name

    def get_size(self):
        return len(self.headers)

    def get_headers(self):
        return self.headers

    def get_type(self):
        return self.type

    def randomize(self, headers):
        common.usedRandomize()
        _annotation = annotation()
        _annotation.randomize()
        self.annotation = _annotation
        self.name = self.generate_name()
        self.headers = randomizer.sample(headers, randomizer.randint(0, len(headers)))

    def generate_name(self):
        return common.get_random_string(self.name_length, True) + '_union'

    def generate_code(self):
        code = ''
        if self.annotation is not None:
            code = self.annotation.generate_code() + ' '
        code += 'header_union' + ' '
        code += self.name + ' '
        code += '{\n'
        for header in self.headers:
            name = header.get_name() + '_' + common.get_random_string(self.name_length, False)
            code += '\t' + header.generate_code_ref() + ' ' + name + '; \n'
        code += '}\n'
        return code

    def generate_code_ref(self):
        code = ''
        if self.annotation is not None:
            code = self.annotation.generate_code() + ' '
        code += self.name
        return code