using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;
using System.Windows.Controls;

using Lune.Views;
using Lune.ViewModels;

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
                case "Albums":
                    _libraryDisplay.Children.Add(new v_albums());
                    break;
                case "Songs":
                    v_songs2 songs = new v_songs2();
                    songs.getDatagrid().ItemsSource = _vm.getSongsDisplayed();
                    songs.DataContext = _vm;
                    _libraryDisplay.Children.Add(songs);
                    break;
                default:
                    _libraryDisplay.Children.Add(new v_artists());
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
