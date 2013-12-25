using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Text;
using System.Linq;
using System.Threading.Tasks;

namespace Lune
{
    class Library //this class I don't even
    {
        private List<Album> AlbumLibrary;
        private List<Song> SongLibrary;
        private List<Artist> ArtistLibrary;
        public Library()
        {
            AlbumLibrary = new List<Album>();
            SongLibrary = new List<Song>();
            ArtistLibrary = new List<Artist>();

            //this code is going to move else where in the future, because we will be loading the library from the database instead.
            //right now, it scans folders every time the app is opened
            MediaFiles files = new MediaFiles(this);
            if (Properties.Settings.Default.LibraryPaths != null && Properties.Settings.Default.LibraryPaths.Count > 0)
            {
                //this loop goes through all directories listed in user settings for folders to add to the library
                foreach (string path in Properties.Settings.Default.LibraryPaths)
                {
                    files.scrapper(path);
                }
            }
        }
        public List<Artist> GetArtists()
        {
            return ArtistLibrary;
        }
        public List<Album> GetAlbums()
        {
            return AlbumLibrary;
        }
        public List<Song> GetSongs()
        {
            return SongLibrary;
        }
        public void Add(object something)
        {
            if (something is Song ){
                SongLibrary.Add((Song)something);
            }
            else if (something is Album)
            {
                AlbumLibrary.Add((Album)something);
            }
            else if (something is Artist)
            {
                ArtistLibrary.Add((Artist)something);
            }
        }
    }
}
