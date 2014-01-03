using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Media.Imaging;
using TagLib;

namespace Lune
{
    /* this is the song class. with just a file path, 
     it uses the taglib library to get track infos
     TODO: there's a lot to do.
     */
    class Song : INotifyPropertyChanged
    {
        private string _name;
        public string path {get; set; }
        public string name { get { return _name; } set { _name = value; OnPropertyChanged("name"); } }
        public int trackN {get; set; }
        public Album album { get; set; }
        public Artist artist { get { return album.artist; } set {album.artist = value;} }
        public TimeSpan Duration { get; private set; }

        public string ArtistName { get { return artist.getName(); } set { } }


        public Song(string path)
        {
            this.path = path;

            try
            {
                TagLib.File f = TagLib.File.Create(path);
                _name = f.Tag.Title;
                trackN = Convert.ToInt32(f.Tag.Track);
                Duration = f.Properties.Duration;
                album = new Album(f.Tag.Album); //probably inadequate
                artist = new Artist(f.Tag.FirstAlbumArtist);//probably inadequate
            }
            catch (Exception e)
            {
                name = "unknown";
                trackN = 0;
            }
        }

        public MemoryStream getImage()
        {
            TagLib.File f = TagLib.File.Create(path);
            TagLib.IPicture pic = null;
            try
            {
                pic = f.Tag.Pictures[0];
                return new MemoryStream(pic.Data.Data);
            }
            catch (Exception e) { }
            return null;

        }

        public override string ToString()
        {
            return trackN + " - " + name;
        }

        public event PropertyChangedEventHandler PropertyChanged;
        protected virtual void OnPropertyChanged(string propertyName)
        {
            PropertyChangedEventHandler handler = PropertyChanged;
            if (handler != null) handler(this, new PropertyChangedEventArgs(propertyName));
        }
        protected bool SetField<T>(ref T field, T value, string propertyName)
        {
            if (EqualityComparer<T>.Default.Equals(field, value)) return false;
            field = value;
            OnPropertyChanged(propertyName);
            return true;
        }

    }
}
