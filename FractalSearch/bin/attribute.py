class Attribute(object):
    def __init__(self, col_name, col_type, unique_values):
        self.col_name = col_name
        self.col_type = col_type
        self.unique_values = unique_values
