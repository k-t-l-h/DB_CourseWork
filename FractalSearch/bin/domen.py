from bin.table import Table
import bin.methods as cfg


class Domen(object):
    def __init__(self, table, atr_idx):
        self.atr_idx = atr_idx
        columns = table.get_columns()
        atr_list = [columns[x].col_name for x in atr_idx]
        self.unique_values = cfg.get_unique_values(table.table_name, atr_list)

    def get_atr_idx(self):
        return self.atr_idx
