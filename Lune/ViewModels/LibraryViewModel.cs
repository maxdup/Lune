using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;
using System.Diagnostics;

using Lune.Commands;
using Lune;
using System.Windows.Documents;
namespace Lune.ViewModels
{
    internal class LibraryViewModel
    {
        Player _playah;
        Library _lib;

        List<Song> _songsDisplayed;
        List<Album> _albumsDisplayed;
        List<Artist> _artistsDisplayed;

        public LibraryViewModel(Player player)
        {
            _playah = player;
            _lib = new Library();
            
            _songsDisplayed = _lib.GetSongs();
            _albumsDisplayed = _lib.GetAlbums();
            //_artistsDisplayed = _lib.GetArtists(); uncomment when implemented
        }

        public void Play(object sender)//this method 
        {
            _playah.setQueue(new SongQueue(_songsDisplayed));
            _playah.Start();
        }

        public List<Song> getSongsDisplayed()
        {
            return _songsDisplayed;
        }
    }
}
