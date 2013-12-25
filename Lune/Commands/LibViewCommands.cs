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
        Panel _libraryDisplay;

        public LibViewCommands(LibraryViewModel vm, Panel panel)
        {
            _vm = vm;
            _libraryDisplay = panel;
        }

        public bool CanExecute(object parameter)
        {
            return true;
        }

        public void Execute(object parameter)
        {
            _libraryDisplay.Children.Clear();

            switch ((string)parameter)
            {
                case "Settings":
                    v_LibrarySubsetting libsubset = new v_LibrarySubsetting();
                    UserSettingsViewModel uSettingVM = new UserSettingsViewModel(libsubset);
                    libsubset.DataContext = uSettingVM;
                    _libraryDisplay.Children.Add(libsubset);
                    break;

                case "Albums":
                    v_albums albums = new v_albums();
                    albums.DataContext = _vm;
                    _libraryDisplay.Children.Add(albums);
                    break;

                case "Songs":
                    v_songs2 songs = new v_songs2();
                    songs.DataContext = _vm;
                    _libraryDisplay.Children.Add(songs);
                    break;

                default:
                    v_artists artists = new v_artists();
                    artists.DataContext = _vm;
                    _libraryDisplay.Children.Add(artists);
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
