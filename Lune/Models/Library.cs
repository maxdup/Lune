using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Text;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Data;
using System.ComponentModel;
using System.Collections.ObjectModel;

namespace Lune
{

    class Library : INotifyPropertyChanged //this class I don't even
    {
        public ObservableCollection<Song> SongLibrary { get; set; }
        public ObservableCollection<Album> AlbumLibrary { get; set; }
        public ObservableCollection<Artist> ArtistLibrary { get; set; }

        private static object _lock = new object();

        public Library()
        {

            ArtistLibrary = new ObservableCollection<Artist>();
            AlbumLibrary = new ObservableCollection<Album>();
            SongLibrary = new ObservableCollection<Song>();

            BindingOperations.CollectionRegistering += BindingOperations_CollectionRegistering;

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

        private void BindingOperations_CollectionRegistering(object sender, CollectionRegisteringEventArgs e)
        {
            BindingOperations.EnableCollectionSynchronization(ArtistLibrary, _lock);
            BindingOperations.EnableCollectionSynchronization(AlbumLibrary, _lock);
            BindingOperations.EnableCollectionSynchronization(SongLibrary, _lock);
        }
    }
}
