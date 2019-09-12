from bin_mod.table import Table
import bin_mod.methods as cfg


class Domen(object):
    def __init__(self, table, atr_idx):
        self.atr_idx = atr_idx
        columns = table.get_columns()
        self.atr_list = [columns[x] for x in atr_idx]
        self.unique_values = 0
        self.dict = []

    def get_atr_idx(self):
        return self.atr_idx

    def try_to_put(self, val):
        if val not in self.dict:
            self.dict.append(val)
            self.unique_values += 1
