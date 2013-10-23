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
        public string ToString()
        //formated to be used in sql inserts/updates ex:"(name)"
        {
            return "(" + name + ", " + artist.getId() + ", " + label.getId() + ")";
        }
    }
}
