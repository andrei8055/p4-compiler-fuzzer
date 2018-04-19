class struct(object):
    annotation = None
    name = ''
    fields = []
    type = 'struct'
    base_type = 'struct'

    def __init__(self, annotation, name, fields):
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