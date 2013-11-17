using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
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
            files.scrapper("D:\\Music\\"); //insert w/e directory you wish to scan
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
