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
        public Library()
        {
            AlbumLibrary = new List<Album>();
            SongLibrary = new List<Song>();

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
        }
                    
    }
}
