using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using TagLib;

namespace Lune
{
    /* this is the song class. with just a file path, 
     it uses the taglib library to get track infos
     TODO: there's a lot to do.
     */
    class Song
    {
        public string path {get; set; }
        public string name { get; set; }
        public int trackN {get; set; }
        public Album album { get; set; }
        public Artist artist { get; set; }


        public Song(string path)
        {
            this.path = path;

            try
            {
                TagLib.File f = TagLib.File.Create(path);
                name = f.Tag.Title;
                trackN = Convert.ToInt32(f.Tag.Track);
                album = new Album(f.Tag.Album);
                artist = new Artist(f.Tag.FirstAlbumArtist);
            }
            catch (Exception e)
            {
                name = "unknown";
                trackN = 0;
            }
        }
        
        public override string ToString()
        {
            return trackN + " - " + name;
        }
    }
}
