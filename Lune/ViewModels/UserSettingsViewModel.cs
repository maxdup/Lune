using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;
using System.Collections.Specialized;
using System.Collections.ObjectModel;
using System.Windows.Controls;

using Lune.Commands;
using Lune.Views;
using Lune.ViewModels;


namespace Lune.ViewModels
{
    class UserSettingsViewModel
    {
        public ObservableCollection<string> paths { get; set; }
        public ICommand settingsCtrl { get; private set; }

        public UserSettingsViewModel(LibraryViewModel LibVm)
        {
            settingsCtrl = new SettingsCommands(this, LibVm);
            paths = new ObservableCollection<string>(Properties.Settings.Default.LibraryPaths.Cast<string>());
            
        }
    }
}
