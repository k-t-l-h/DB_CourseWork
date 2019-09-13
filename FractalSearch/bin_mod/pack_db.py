import pyodbc
from bin_mod.domen_collection import DomenCollection
from bin_mod.table import Table
import bin_mod.methods as cfg


def pack(table_name, max_domen_length):
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=' + cfg.server +
                          ';Database=' + cfg.db +
                          ';Trusted_Connection=yes;')
    domen_collection = DomenCollection(Table(table_name), max_domen_length)
    cursor = conn.cursor()

    sql_command = "CREATE TABLE " + table_name + "_modpacked \
    (id int IDENTITY(1,1) PRIMARY KEY,\n"

    domens = domen_collection.opt_collection.domens

    for i in range(len(domens)):
        sql_command += "domen" + str(i + 1)
        if len(domens[i].atr_idx) > 1:
            sql_command += " int"
        else:
            sql_command += " nvarchar(255)"
        if i != len(domens) - 1:
            sql_command += ",\n"
        else:
            sql_command += ")"

    rows = domen_collection.opt_collection.pack()
    cursor.execute(sql_command)
    #conn.commit()
    for x in rows:
        sql_command = "INSERT INTO " + table_name + "_modpacked VALUES " + x
        cursor.execute(sql_command)
    #conn.commit()
    conn.close()

    output_f = open("F:\\DB_CourseWork\\FractalSearch\\bin_mod\\"+table_name+"dicts.txt", "w")
    for domen in domen_collection.opt_collection.domens:
        for x in domen.atr_list:
            output_f.write(x.col_name + " " + str(x.col_type))
            output_f.write("\n")
        for x in domen.dict:
            output_f.write(str(x) + "\n")
        output_f.write('---\n')
    output_f.close()
