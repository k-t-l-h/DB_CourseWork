import pyodbc
import bin_mod.methods as cfg
from bin_mod.attribute import Attribute


class Table(object):
    def __init__(self, table_name):
        self.server = cfg.server
        self.db = cfg.db
        self.table_name = table_name
        meta = cfg.get_cursor()
        meta.execute("SELECT  * FROM " + table_name)
        self.columns = [Attribute(x[0], x[1], cfg.get_unique_values(table_name, [x[0]])) for x in meta.description[1:]]
        self.length = len(meta.fetchall())

    def get_columns(self):
        return self.columns

    def get_data(self):
        cursor = cfg.get_cursor()
        cursor.execute("SELECT  * FROM " + self.table_name)
        return cursor.fetchall()