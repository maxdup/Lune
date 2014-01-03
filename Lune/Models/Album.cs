using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Controls;
using System.Windows.Media.Imaging;

namespace Lune
{
    class Album
    {
        int id;
        int year;
        public string name { get; set; }
        public Label label { get; set; }
        public Artist artist { get; set; }
        public Image Artwork { get { return getImage(); } set {} }
        LinkedList<Song> songs;

        public Album() : this("unknown") {}
        public Album(string name) : this (name, new Artist("unknown"),new Label("unknown"), 0)  {}
        public Album(string name, Artist artist, Label label, int year)
        {
            this.name = name;
            this.artist = artist;
            this.label = label;
            this.year = year;
        }
        public void AddSong(Song song)
        {
            if (songs == null)
            {
                songs = new LinkedList<Song>();
            }
            songs.AddLast(song);
        }
        public int getId()
        {
            return id;
        }
        public override string ToString()
        {
            return name;
        }
        public Image getImage()
        {
            Image img = new Image();
            if(songs != null){
                // Load you image data in MemoryStream
                MemoryStream ms = songs.ElementAt(0).getImage();
                if (ms != null)
                {
                    ms.Seek(0, SeekOrigin.Begin);

                    // ImageSource for System.Windows.Controls.Image
                    BitmapImage bitmap = new BitmapImage();
                    bitmap.BeginInit();
                    bitmap.StreamSource = ms;
                    bitmap.EndInit();

                    img.Source = bitmap;
                }
            }
            return img;
        }
    }
}
