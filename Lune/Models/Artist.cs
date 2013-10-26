using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lune
{
    //this is mostly a placeholder
    class Artist
    {
        int id;
        string name;
        LinkedList<Album> albums;
        public Artist() : this("unknown"){}
        public Artist(string name)
        {
            this.name = name;
        }
        public string getName()
        {
            return name;
        }
        public int getId()
        {
            return id;
        }

        public override string ToString()
        //formated to be used in sql inserts/updates ex:"(name)"
        {
            return "('" + name + "')";
        }
    }
}
