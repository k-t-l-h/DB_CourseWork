import pyodbc

server = 'DESKTOP-9C01EOF\SQLEXPRESS'
db = 'test'


def get_unique_values(table_name, atr_list):
    cursor = get_cursor()
    command_line = "SELECT "
    if len(atr_list) > 1:
        command_line += ", ".join(atr_list)
    else:
        command_line += atr_list[0]
    command_line += " FROM " + table_name
    cursor.execute(command_line)

    row = cursor.fetchone()
    result = []
    while row:
        value = [x for x in row]
        if value not in result:
            result.append(value)
        row = cursor.fetchone()

    return len(result)


def get_cursor():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=' + server +
                          ';Database=' + db +
                          ';Trusted_Connection=yes;')
    return conn.cursor()

