using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;
using System.Diagnostics;
using System.Windows.Documents;
using System.Windows.Controls;
using System.ComponentModel;
using System.Collections.ObjectModel;

using Lune.Commands;
using Lune;

namespace Lune.ViewModels
{
    internal class LibraryViewModel : INotifyPropertyChanged
    {
        Player _playah;

        public ObservableCollection<Song> songsDisplayed { get; set; }
        public ObservableCollection<Album> albumsDisplayed { get; set; }
        public ObservableCollection<Artist> artistsDisplayed { get; set; }

        public Panel MainPanel { get; set; }
        public TabControl libraryDisplay {get; set;}

        public Library lib { get; private set; }

        public ICommand libViews { get; private set; }

        public LibraryViewModel(Player player, Panel panel)
        {
            MainPanel = panel;
            libraryDisplay = MainPanel.Children.OfType<TabControl>().ElementAt(0);
            _playah = player;
            lib = new Library();

            resetFilters();

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
                _playah.setQueue(new SongQueue(songsDisplayed.ToList<Song>(), startAt));
                _playah.Start();
            }
        }
        public void artistFilter(string ArtistName)
        {
            albumsDisplayed = new ObservableCollection<Album>(lib.AlbumLibrary.Where(x => x.artist.getName() == ArtistName));
            songsDisplayed = new ObservableCollection<Song>(lib.SongLibrary.Where(x => x.artist.getName() == ArtistName));
            PropertyChange("songsDisplayed");
            PropertyChange("albumsDisplayed");
        }
        public void albumFilter(string AlbumName)
        {
            songsDisplayed = new ObservableCollection<Song>(lib.SongLibrary.Where(x => x.album.name == AlbumName));
            PropertyChange("songsDisplayed");
        }
        public void resetFilters()
        {
            songsDisplayed = lib.SongLibrary;
            albumsDisplayed = lib.AlbumLibrary;
            artistsDisplayed = lib.ArtistLibrary;
        }

        public event PropertyChangedEventHandler PropertyChanged;

        public void PropertyChange(string prop)
        {
            if (PropertyChanged != null)
            {
                PropertyChanged(this, new PropertyChangedEventArgs(prop));
            }
        }
    }
}
