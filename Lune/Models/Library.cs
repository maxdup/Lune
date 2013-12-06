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

            //this loop goes through all directories listed in user settings for folders to add to the library
            List<String> paths;
            if (Properties.Settings.Default.LibraryPaths != null)
            {
                paths = new List<string>(Properties.Settings.Default.LibraryPaths.Cast<string>());
                if (paths.Count != 0)
                {
                    foreach (string path in paths)
                    {
                        files.scrapper(path);
                    }
                }
            }
            files.scrapper("F:\\music"); //quick and dirty test, remove eventually
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
