from bin.table import Table
from bin.domen import Domen
from bin.opt_collection import OptCollection

MAXDOMEN = 3


def next_domen(iterator, length):
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


def filter_domens_by_first_attribute(domens, atr_idx):
    result = []
    for x in domens:
        if x.get_atr_idx()[0] == atr_idx:
            result.append(x)

    return result


def check_atr_in_collection(atr_idx, domens):
    for x in domens:
        if atr_idx in x.atr_idx:
            return True
    return False


def generate_optimal_collection(table, domens, columns_count):
    init = filter_domens_by_first_attribute(domens, 0)
    prev_result = []
    result = []
    for x in init:
        prev_result.append([x])
    for i in range(2, columns_count):
        result = []
        tmp = filter_domens_by_first_attribute(domens, i)
        for collection in prev_result:
            if not check_atr_in_collection(i, collection):
                for x in tmp:
                    result.append(collection+[x])
            else:
                result.append(collection)
        prev_result = result

    collections = [OptCollection(table, x) for x in result]
    opt_collection = None
    for x in collections:
        if x.check_fullness():
            if opt_collection is None:
                opt_collection = x
            elif x.get_unique_values() < opt_collection.get_unique_values():
                opt_collection = x

    return opt_collection


class DomenCollection(object):
    def __init__(self, table):
        self.table = table
        # all domens
        columns = table.get_columns()
        columns_count = len(columns)
        domens = []
        for length in range(2,MAXDOMEN+1):
            iterator = [x for x in range(0,length)]
            while iterator[0] <= columns_count - length:
                domens.append(Domen(table, [x for x in iterator]))
                iterator = next_domen(iterator, columns_count)
        self.domens = domens
        # all opt collections
        self.opt_collection = generate_optimal_collection(table, domens, columns_count)


dc = DomenCollection(Table("TestTable"))
print(dc.opt_collection)
