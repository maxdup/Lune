using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lune
{
    class Library
    {
        private List<Song> SongLibrary;
        public Library()
        {

        }
        public List<Song> GetLibrary()
        {
            return SongLibrary;
        }
    }
}
