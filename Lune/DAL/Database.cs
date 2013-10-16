using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SQLite;
using System.Data;

namespace Lune
{
    class Database
    {
        private SQLiteConnection sql_conn;
        private SQLiteCommand sql_cmd;
        private SQLiteDataAdapter DB;
        private DataSet DS = new DataSet();
        private DataTable DT = new DataTable();
        public Database()
        {
            //this constructor checks if the database exists and creates one if misisng
            sql_conn = new SQLiteConnection("Data Source=lune.ldb;Version=3;FailIfMissing=True;");
            try
            {
                sql_conn.Open();
            }
            catch (SQLiteException)
            {
                DbInit();
            }
            finally
            {
                sql_conn.Close();
            }
        }
        public void DbInit()
        /* this method initializes the database.
         * note: it's probably not a good idea to call
         * this method if the database already exists.
         */
        {
            sql_conn = new SQLiteConnection("Data Source=lune.db;Version=3;New=True");
            sql_conn.Open();
            sql_cmd.CommandText = "Create table ";
            sql_conn.Close();
        }
    }
}
