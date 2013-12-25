using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;
using System.Diagnostics;
using System.Windows.Documents;
using System.Windows.Controls;

using Lune.Commands;
using Lune;

namespace Lune.ViewModels
{
    internal class LibraryViewModel
    {
        Player _playah;
        Library _lib;

        public List<Song> songsDisplayed{ get; set;}
        public List<Album> albumsDisplayed{ get; set;}
        public List<Artist> artistsDisplayed { get; set; }

        Panel _libraryDisplay;

        public ICommand libViews { get; private set; }

        public LibraryViewModel(Player player, Panel panel)
        {
            _libraryDisplay = panel;
            _playah = player;
            _lib = new Library();
            
            songsDisplayed = _lib.GetSongs();
            albumsDisplayed = _lib.GetAlbums();
            artistsDisplayed = _lib.GetArtists();

            libViews = new LibViewCommands(this, _libraryDisplay);
        }

        public void Play(object sender)
        {
            _playah.setQueue(new SongQueue(songsDisplayed, ((DataGridRow)sender).GetIndex()));
            _playah.Start();
        }

        public List<Song> getSongsDisplayed()
        {
            return songsDisplayed;
        }
    }
}
