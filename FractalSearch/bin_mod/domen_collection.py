from bin_mod.table import Table
from bin_mod.domen import Domen
from bin_mod.opt_collection import OptCollection
import time

MAXDOMEN = 3


def next_domen(iterator, length, skip):
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

    return check_domen(iterator, length, skip)


def check_domen(iterator, length, skip):
    for x in iterator:
        if x in skip:
            return next_domen(iterator, length, skip)
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


def get_full_collections(table, packable_domens, unpackable_atr, columns_count):
    result = []
    prev_result = []
    if len(unpackable_atr) > 0:
        prev_result = [[x] for x in unpackable_atr]
    else:
        for x in filter_domens_by_first_attribute(packable_domens, 0):
            prev_result.append([x])
    for i in range(columns_count):
        result = []
        tmp = filter_domens_by_first_attribute(packable_domens, i)
        for collection in prev_result:
            if not check_atr_in_collection(i, collection):
                for x in tmp:
                    flag = False
                    for idx in x.atr_idx:
                        flag = check_atr_in_collection(idx, collection)
                    if not flag:
                        result.append(collection+[x])
            else:
                result.append(collection)
        if len(result) > 0:
            prev_result = result
    if len(result) == 0:
        result = prev_result
    collections = [OptCollection(table, x) for x in result]
    opt_collections = []
    for x in collections:
        if x.check_fullness():
            opt_collections.append(x)

    return opt_collections


def fill_collections(table, collections):
    domens = []
    for collection in collections:
        for domen in collection.domens:
            if domen not in domens:
                domens.append(domen)


    dataset = table.get_data()
    for row in dataset:
        for domen in domens:
            if len(domen.atr_idx) == 1:
                domen.try_to_put(row[domen.atr_idx[0]])
            else:
                value = [row[idx] for idx in domen.atr_idx]
                domen.try_to_put(value)


def get_min_collection(collections):
    result = collections[0]
    count = result.get_unique_values()

    for x in collections:
        if x.get_unique_values() < count:
            result = x
            count = result.get_unique_values()

    return result


class DomenCollection(object):
    def __init__(self, table, max_domen_length):
        self.table = table
        # all domens
        columns = table.get_columns()
        columns_count = len(columns)
        packable_domens = []
        unpackable_atr = []
        skip = []
        # get unpackable attributes
        for i in range(len(columns)):
            if not columns[i].is_packable(table.length):
                unpackable_atr.append(Domen(table, [i]))
                skip.append(i)
        # get all packable domens
        for length in range(1, min(max_domen_length+1, len(columns))):
            iterator = [x for x in range(0, length)]
            iterator = check_domen(iterator, length, skip)
            while iterator[0] <= columns_count - length:
                packable_domens.append(Domen(table, [x for x in iterator]))
                iterator = next_domen(iterator, columns_count, skip)
        self.domens = packable_domens + unpackable_atr
        # all full collections
        full_collections = get_full_collections(table, packable_domens, unpackable_atr, columns_count)
        fill_collections(table, full_collections)
        self.opt_collection = get_min_collection(full_collections)
