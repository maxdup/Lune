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
        Panel _libraryDisplay {  get { return _vm.libraryDisplay; } set {} }
        UIElementCollection UIonHold;

        public LibViewCommands(LibraryViewModel vm)
        {
            _vm = vm;
        }

        public bool CanExecute(object parameter)
        {
            return true;
        }

        public void Execute(object parameter)
        {
            UIElementCollection returnUI = _vm.MainPanel.Children;
            _libraryDisplay.Children.Clear();
            _vm.resetFilters();
            switch ((string)parameter)
            {
                case "back":
                    _vm.MainPanel.Children.Clear();
                    foreach(Panel ele in UIonHold){
                        _vm.MainPanel.Children.Add(ele);
                    }
                    break;
                case "Settings":
                    UIonHold = returnUI;
                    v_LibrarySubsetting libsubset = new v_LibrarySubsetting();
                    UserSettingsViewModel uSettingVM = new UserSettingsViewModel(libsubset);
                    libsubset.DataContext = uSettingVM;
                    _vm.MainPanel.Children.Clear();
                    _vm.MainPanel.Children.Add(libsubset);
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
