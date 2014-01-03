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
using System.ComponentModel;

namespace Lune.ViewModels
{
    internal class LibraryViewModel : INotifyPropertyChanged
    {
        Player _playah;
        Library _lib;

        private List<Song> _songsDisplayed;
        private List<Album> _albumsDisplayed;
        private List<Artist> _artistsDisplayed;
        public List<Song> songsDisplayed { get { return _songsDisplayed; } set { _songsDisplayed = value; PropertyChange("songsDisplayed"); } }
        public List<Album> albumsDisplayed { get{ return _albumsDisplayed; } set { _albumsDisplayed = value; PropertyChange("albumsDisplayed"); } }
        public List<Artist> artistsDisplayed { get; set; }

        public Panel MainPanel { get; set; }
        public Panel libraryDisplay {get; set;}

        public ICommand libViews { get; private set; }

        public LibraryViewModel(Player player, Panel panel)
        {
            MainPanel = panel;
            libraryDisplay = MainPanel.Children.OfType<DockPanel>().ElementAt(1);//if something breaks someday, blame this line
            _playah = player;
            _lib = new Library();
            
            songsDisplayed = _lib.GetSongs();
            albumsDisplayed = _lib.GetAlbums();
            artistsDisplayed = _lib.GetArtists();

            libViews = new LibViewCommands(this);
        }

        public void Play(object sender)
        {
            int startAt = 0;
            if (sender is DataGridRow){
                startAt = ((DataGridRow)sender).GetIndex();
            }else if (sender is ListBox){
                startAt = ((ListBox)sender).SelectedIndex;
            }else if (sender is ListBoxItem){//I would much prefer if the event was handled by items but...
                //???
            }
            if (startAt != -1)
            {
                _playah.setQueue(new SongQueue(songsDisplayed, startAt));
                _playah.Start();
            }
        }
        public void artistFilter(string ArtistName)
        {
            albumsDisplayed = _lib.GetAlbums().Where(x => x.artist.getName() == ArtistName).ToList();
            songsDisplayed = _lib.GetSongs().Where(x => x.artist.getName() == ArtistName).ToList();
        }
        public void albumFilter(string AlbumName)
        {
            songsDisplayed = _lib.GetSongs().Where(x => x.album.name == AlbumName).ToList();
        }
        public void resetFilters()
        {
            songsDisplayed = _lib.GetSongs();
            albumsDisplayed = _lib.GetAlbums();
            artistsDisplayed = _lib.GetArtists(); // may or may not be needed depending on views developed in the future
        }

        public event PropertyChangedEventHandler PropertyChanged;

        private void PropertyChange(string prop)
        {
            if (PropertyChanged != null)
            {
                PropertyChanged(this, new PropertyChangedEventArgs(prop));
            }
        }
    }
}
