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
<<<<<<< HEAD
            sql_conn = new SQLiteConnection("Data Source=lune.ldb;Version=3;FailIfMissing=True;");
            try
=======
            sql_conn = new SQLiteConnection("Data Source=lune.dbl;Version=3;FailIfMissing=True;");
            try 
>>>>>>> basic database setup
            {
                //checks if the database can be opened (todo: probably should also check that the schema is correct and up to date)
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
         * this method if the database already exists. (probably overwrites it)
         */
        {
            sql_conn = new SQLiteConnection("Data Source=lune.dbl;Version=3;New=True");
            sql_conn.Open();
            sql_cmd = new SQLiteCommand(
                "create table Artist (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT);" +
                "create table Label (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT);" +
                "create table Album (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, idArtist int, idLabel int, FOREIGN KEY (idArtist) references Artist(id), FOREIGN KEY (idLabel) references Label(id));" +
                "create table Song (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, trackNb int, path Text, idAlbum int, FOREIGN KEY (idAlbum) references Album(id));", sql_conn);
            sql_cmd.ExecuteNonQuery();
        }

        public void addSong(Song song)
        {
            sql_conn.Open();
            sql_cmd = new SQLiteCommand("insert into Song (name, trackNb, path, idAlbum) values " + song.ToString(), sql_conn);
            sql_cmd.ExecuteNonQuery();
        }
        public void addAlbum(Album album)
        {
            sql_conn.Open();
            sql_cmd = new SQLiteCommand("insert into Album (name, idArtist, idLabel) values " + album.ToString(), sql_conn);
            sql_cmd.ExecuteNonQuery();
        }
        public void addArtist(Artist artist)
        {
            sql_conn.Open();
            sql_cmd = new SQLiteCommand("insert into Artist (name) values " + artist.ToString(), sql_conn);
            sql_cmd.ExecuteNonQuery();
        }
        public void addLabel(Label label)
        {
            sql_conn.Open();
            sql_cmd = new SQLiteCommand("insert into Label (name) values " + label.ToString(), sql_conn);
            sql_cmd.ExecuteNonQuery();
        }
    }
}
