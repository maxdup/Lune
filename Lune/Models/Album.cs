﻿using System;
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
        string name;
        Label label = new Label();
        Artist artist = new Artist();
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
