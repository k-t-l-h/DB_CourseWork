using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;
using System.Data.SqlClient;

namespace FractalSearch
{
    class Table
    {
        List<Attribute> Column;
        int TableSize;
        string TableName;

        public testDataSet get_Table()
        {
            return new testDataSet();
        }

        public DataTableReader get_Data()
        {
            testDataSet set = new testDataSet();
            return set.CreateDataReader();
        }
    }
}
