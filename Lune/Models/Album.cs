using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lune
{
    //this is mostly a placeholder
    class Album
    {
        int id;
        int year;
        string name;
        Label label = new Label();
        Artist artist = new Artist();
        LinkedList<Song> songs;

        public Album() : this("unknown") {}
        public Album(string name)
        {
            this.name = name;
        }
        public int getId()
        {
            return id;
        }
        public string getName()
        {
            return name;
        }
        public Artist getArtist()
        {
            return artist;
        }
        public Label getLabel()
        {
            return label;
        }
        public string ToString()
        {
            return name;
        }
    }
}
