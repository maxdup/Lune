using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;
using System.Windows.Controls;

using Lune.Views;
using Lune.ViewModels;
using System.Collections.ObjectModel;

namespace Lune.Commands
{
    internal class LibViewCommands : ICommand
    {
        LibraryViewModel _vm;
        TabControl _libraryDisplay {  get { return _vm.libraryDisplay; } set {} }
        

        public LibViewCommands(LibraryViewModel vm)
        {
            _vm = vm;

            v_artists artists = new v_artists();
            artists.DataContext = _vm;
            _libraryDisplay.Items.Add(artists);

            v_albums albums = new v_albums();
            albums.DataContext = _vm;
            _libraryDisplay.Items.Add(albums);

            v_songs2 songs = new v_songs2();
            songs.DataContext = _vm;
            _libraryDisplay.Items.Add(songs);
        }

        public bool CanExecute(object parameter)
        {
            return true;
        }

        public void Execute(object parameter)
        {
            _vm.resetFilters();
            switch ((string)parameter)
            {
                case "Albums":
                    _libraryDisplay.SelectedIndex = 1;
                    ((v_albums)_libraryDisplay.SelectedValue).listB_Albums.Items.Refresh();
                    break;

                case "Songs":
                    _libraryDisplay.SelectedIndex = 2;
                    ((v_songs2)_libraryDisplay.SelectedValue).listB_Songs.Items.Refresh();
                    break;

                default:// "Artist"
                    _libraryDisplay.SelectedIndex = 0;
                    ((v_artists)_libraryDisplay.SelectedValue).syncToLib();
                    _vm.PropertyChange("songsDisplayed");
                    _vm.PropertyChange("albumsDisplayed");
                    _vm.PropertyChange("artistDisplayed");
                    ((v_artists)_libraryDisplay.SelectedValue).listB_Artists.Items.Refresh();
                    break;
            }
        }
        public event EventHandler CanExecuteChanged
        {
            add { CommandManager.RequerySuggested += value; }
            remove { CommandManager.RequerySuggested -= value; }
        }
    }
}
