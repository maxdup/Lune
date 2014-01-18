using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Text;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Data;
using System.ComponentModel;

namespace Lune
{

    class Library : INotifyPropertyChanged //this class I don't even
    {
        private List<Song> _SongLibrary;
        private List<Album> _AlbumLibrary;
        private List<Artist> _ArtistLibrary;

        public List<Song> SongLibrary { get { return _SongLibrary; } set { _SongLibrary = value; PropertyChange("SongLibrary"); } }
        public List<Album> AlbumLibrary { get { return _AlbumLibrary; } set { _AlbumLibrary = value; PropertyChange("AlbumLibrary"); } }
        public List<Artist> ArtistLibrary { get { return _ArtistLibrary; } set { _ArtistLibrary = value; PropertyChange("ArtistLibrary"); } }

        private static object _lock = new object();

        public Library()
        {
            AlbumLibrary = new List<Album>();
            SongLibrary = new List<Song>();
            ArtistLibrary = new List<Artist>();

            BindingOperations.EnableCollectionSynchronization(ArtistLibrary, _lock);
            BindingOperations.EnableCollectionSynchronization(AlbumLibrary, _lock);
            BindingOperations.EnableCollectionSynchronization(SongLibrary, _lock);

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

        public event PropertyChangedEventHandler PropertyChanged;

        public void PropertyChange(string prop)
        {
            if (PropertyChanged != null)
            {
                PropertyChanged(this, new PropertyChangedEventArgs(prop));
            }
        }
    }
}
