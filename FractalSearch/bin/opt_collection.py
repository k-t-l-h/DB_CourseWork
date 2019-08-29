from bin.domen import Domen


class OptCollection(object):
    @staticmethod
    def check_full(table, domens):
        columns = table.get_columns()
        num = [0 for x in columns]

        for domen in domens:
            for idx in domen.atr_idx:
                num[idx] += 1

        for i in num:
            if i != 1:
                return False
        return True

    def __init__(self, table, domens):
        self.table = table
        self.domens = domens
        self.is_full = self.check_full(table, domens)

    def write(self):
        return 0
