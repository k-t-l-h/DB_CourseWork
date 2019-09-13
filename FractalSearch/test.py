import time
import bin.pack_db as pack
import bin_mod.pack_db as pack_mod

tb = time.process_time()
pack.pack("TestTable", 3)
tm = time.process_time()
print(tm-tb)
pack_mod.pack("TestTable", 3)
te = time.process_time()
print(te-tm)
