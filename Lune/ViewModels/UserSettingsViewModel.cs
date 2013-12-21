using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;

using Lune.Commands;
using Lune.Views;
using System.Collections.Specialized;
using System.Collections.ObjectModel;

namespace Lune.ViewModels
{
    class UserSettingsViewModel
    {
        public ICommand settings { get; private set; }
        public StringCollection paths{ get; set;}

        public UserSettingsViewModel(v_LibrarySubsetting pathView)
        {
            settings = new SettingsCommands(pathView, this);
            paths = Properties.Settings.Default.LibraryPaths;
        }
    }
}
