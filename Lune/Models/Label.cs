using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lune
{
    //this is mostly a placeholder
    class Label
    {
        private int id;
        private String name;
        LinkedList<Album> albums;

        public Label(): this("unknown"){ }
        public Label(string name)
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
        public string ToString()
        {
            return name;
        }
    }
}
