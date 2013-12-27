using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lune
{
    class Album
    {
        int id;
        int year;
        public string name { get; set; }
        public Label label { get; set; }
        public Artist artist { get; set; }
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
