from bin.table import Table
from bin.domen import Domen
from bin.opt_collection import OptCollection

MAXDOMEN = 3


def nextDomen(iterator, length):
    iterator.reverse()

    iterator[0] += 1
    for x in range(len(iterator)-1):
        if iterator[x] < length-x:
            break
        else:
            iterator[x + 1] += 1
            iterator[x] = 0

    iterator.reverse()

    for x in range(1, len(iterator)):
        if iterator[x] == 0:
            iterator[x] = iterator[x-1] + 1

    return iterator


class DomenCollection(object):
    def __init__(self, table):
        self.table = table
        # all domens
        columns = table.get_columns()
        domens = []
        for length in range(2,MAXDOMEN+1):
            iterator = [x for x in range(1,length+1)]
            while iterator[0] <= len(columns) - length:
                domens.append(Domen(table, [x for x in iterator]))
                iterator = nextDomen(iterator, len(columns))
        self.domens = domens


"""dc = DomenCollection(Table("TestTable"))
print(dc)"""