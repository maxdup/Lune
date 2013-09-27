using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using TagLib;

namespace Lune
{
    /* this is the song class. with just a file path, 
     * it uses the taglib library to get track infos
     TODO: there's a lot to do.
     */
    class Song
    {
        private string path; 
        private string name;
        private uint trackN;

        public Song(string path)
        {
            this.path = path;
            TagLib.File f = TagLib.File.Create(path);
            name = f.Tag.Title;
            trackN = f.Tag.TrackCount;
        }
        public string GetPath()
        {
            return path;
        }
        public string GetName()
        {
            return name;
        }
        public uint GetTrackN()
        {
            return trackN;
        }
    }
}
