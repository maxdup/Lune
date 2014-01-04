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


namespace Lune.ViewModels
{
    class UserSettingsViewModel
    {
        public ObservableCollection<string> paths { get; set; }
        public ICommand settingsCtrl { get; private set; }

        public UserSettingsViewModel(Panel Mainpanel)
        {
            settingsCtrl = new SettingsCommands(this);
            paths = new ObservableCollection<string>(Properties.Settings.Default.LibraryPaths.Cast<string>());
        }
    }
}
