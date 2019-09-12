from bin_mod.domen import Domen


class OptCollection(object):
    @staticmethod
    def check_full(table, domens):
        columns = table.get_columns()
        num = [0 for x in columns]

        for domen in domens:
            for idx in domen.atr_idx:
                num[idx-1] += 1

        for i in num:
            if i != 1:
                return False
        return True

    def __init__(self, table, domens):
        self.table = table
        self.domens = domens
        self.is_full = self.check_full(table, domens)

    def check_fullness(self):
        return self.is_full

    def get_unique_values(self):
        result = 1
        for x in self.domens:
            result *= x.unique_values
        return result

    def pack(self):
        data = self.table.get_data()
        rows = []
        for x in self.domens:
            x.dict = []
        for x in data:
            row = []
            for domen in self.domens:
                value = [x[idx+1] for idx in domen.atr_idx]
                if len(value) > 1:
                    if value in domen.dict:
                        row.append(str(domen.dict.index(value) + 1))
                    else:
                        row.append(str(len(domen.dict) + 1))
                        domen.dict.append(value)
                else:
                    row.append("'" + str(value[0]) + "'")
            rows.append("("+", ".join(row)+")")
        return rows

