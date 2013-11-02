using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SQLite;
using System.Data;
using System.IO;

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
            //this constructor checks if the database exists and creates one if missing
            sql_conn = new SQLiteConnection("Data Source=lune.dbl;Version=3;FailIfMissing=True;");
            try 
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
            if (File.Exists("lune.dbl"))
            {
                File.Delete("lune.dbl");
            }
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
            sql_cmd = new SQLiteCommand("insert into Song (name, trackNb, path, idAlbum) values (@name, @trackn, @path, @AlbId)", sql_conn);
            sql_cmd.Parameters.Add(new SQLiteParameter("@name",song.getName()));
            sql_cmd.Parameters.Add(new SQLiteParameter("@trackn", song.getTrackN().ToString()));
            sql_cmd.Parameters.Add(new SQLiteParameter("@path", song.getPath()));
            sql_cmd.Parameters.Add(new SQLiteParameter("@AlbId", song.getAlbum().getId().ToString()));
            sql_cmd.ExecuteNonQuery();
            sql_conn.Close();
        }
        public void addAlbum(Album album)
        {
            sql_conn.Open();
            sql_cmd = new SQLiteCommand("insert into Album (name, idArtist, idLabel) values (@name, @artId, @labId)", sql_conn);
            sql_cmd.Parameters.Add(new SQLiteParameter("@name", album.getName()));
            sql_cmd.Parameters.Add(new SQLiteParameter("@artId", album.getArtist().getId()));
            sql_cmd.Parameters.Add(new SQLiteParameter("@LabId", album.getLabel().getId()));
            sql_cmd.ExecuteNonQuery();
            sql_conn.Close();
        }
        public void addArtist(Artist artist)
        {
            sql_conn.Open();
            sql_cmd = new SQLiteCommand("insert into Artist (name) values(?)", sql_conn);
            sql_cmd.Parameters.Add(new SQLiteParameter(artist.getName()));
            sql_cmd.ExecuteNonQuery();
            sql_conn.Close();
        }
        public void addLabel(Label label)
        {
            sql_conn.Open();
            sql_cmd = new SQLiteCommand("insert into Label (name) values (?)", sql_conn);
            sql_cmd.Parameters.Add(new SQLiteParameter(label.getName()));
            sql_cmd.ExecuteNonQuery();
            sql_conn.Close();
        }
        public List<Artist> getArtists() //Artist creation incomplete (quick test)
        {
            List<Artist> arts = new List<Artist>();
            DB = new SQLiteDataAdapter("select * from Artist", sql_conn);
            DB.Fill(DT);
            foreach (DataRow row in DT.Rows)
            {
                arts.Add(new Artist(Convert.ToString(row["name"])));// << update constructor when it's done
            }
            return arts;
        }
        public List<Label> getLabels() //Label creation incomplete (quick test)
        {
            List<Label> labels = new List<Label>();
            DB = new SQLiteDataAdapter("select * from Label", sql_conn);
            DB.Fill(DT);
            foreach (DataRow row in DT.Rows)
            {
                labels.Add(new Label(Convert.ToString(row["name"])));// << update constructor when it's done
            }
            return labels;
        }
        public List<Album> getAlbums() //Album creation incomplete (quick test)
        {
            List<Album> albs = new List<Album>();
            DB = new SQLiteDataAdapter("select * from Album", sql_conn);
            DB.Fill(DT);
            foreach (DataRow row in DT.Rows)
            {
                albs.Add(new Album(Convert.ToString(row["name"])));// << update constructor when it's done
            }
            return albs;
        }
    }
}
