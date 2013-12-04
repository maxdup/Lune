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

        List<Song> _songsDisplayed;
        List<Album> _albumsDisplayed;
        List<Artist> _artistsDisplayed;

        Panel _libraryDisplay;

        public ICommand libViews { get; private set; }

        public LibraryViewModel(Player player, Panel panel)
        {
            _libraryDisplay = panel;
            _playah = player;
            _lib = new Library();
            
            _songsDisplayed = _lib.GetSongs();
            _albumsDisplayed = _lib.GetAlbums();
            //_artistsDisplayed = _lib.GetArtists(); uncomment when implemented

            libViews = new LibViewCommands(this, _libraryDisplay);
        }

        public void Play(object sender)
        {
            _playah.setQueue(new SongQueue(_songsDisplayed, ((DataGridRow)sender).GetIndex()));
            DataGridRow dgr = new DataGridRow();
            
            _playah.Start();
        }

        public List<Song> getSongsDisplayed()
        {
            return _songsDisplayed;
        }
    }
}
