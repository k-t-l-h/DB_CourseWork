import pyodbc
from bin.domen_collection import DomenCollection
from bin.table import Table
import bin.methods as cfg


def pack(table_name):
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=' + cfg.server +
                          ';Database=' + cfg.db +
                          ';Trusted_Connection=yes;')
    domen_collection = DomenCollection(Table(table_name))
    cursor = conn.cursor()

    sql_command = "CREATE TABLE " + table_name + "_packed \
    (id int IDENTITY(1,1) PRIMARY KEY,\n"

    domens = domen_collection.opt_collection.domens

    for i in range(len(domens)):
        sql_command += "domen" + str(i + 1) + " int"
        if i != len(domens) - 1:
            sql_command += ",\n"
        else:
            sql_command += ")"

    rows = domen_collection.opt_collection.pack()
    cursor.execute(sql_command)
    conn.commit()
    for x in rows:
        sql_command = "INSERT INTO " + table_name + "_packed VALUES " + x
        cursor.execute(sql_command)
    conn.commit()
    conn.close()

    output_f = open("F:\\DB_CourseWork\\FractalSearch\\bin\\"+table_name+"dicts.txt", "w")
    for domen in domen_collection.opt_collection.domens:
        for x in domen.atr_idx:
            output_f.write(str(x) + " ")
        output_f.write("\n")
        for x in domen.dict:
            output_f.write(" ".join(str(x)) + "\n")
        output_f.write('---\n')
    output_f.close()


base_table_name = "TestCrime1"
pack(base_table_name)
