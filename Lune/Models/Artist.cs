using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lune
{
    class Artist
    {
        int id = 0;
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
        {
            return name;
        }
    }
}
