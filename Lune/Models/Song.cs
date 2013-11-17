﻿using System;
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
        private string path; 
        private string name;
        private int trackN;
        private Album album;

        public Song(string path)
        {
            this.path = path;

            try
            {
                TagLib.File f = TagLib.File.Create(path);
                name = f.Tag.Title;
                trackN = Convert.ToInt32(f.Tag.TrackCount);
            }
            catch (Exception e)
            {
                name = "unknown";
                trackN = 0;
            }
            album = new Album();
            
        }
        public string getPath()
        {
            return path;
        }
        public Album getAlbum()
        {
            return album;
        }
        public string getName()
        {
            return name;
        }
        public int getTrackN()
        {
            return trackN;
        }
        public override string ToString()
        {
            return trackN + " - " + name;
        }
    }
}
