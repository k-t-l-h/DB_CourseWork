import time
import bin.pack_db as pack
import bin_mod.pack_db as pack_mod

table_name = "TestTable"
max_dom = 3

tb = time.process_time()
pack.pack(table_name, max_dom)
tm = time.process_time()
print(tm-tb)
pack_mod.pack(table_name, max_dom)
te = time.process_time()
print(te-tm)
