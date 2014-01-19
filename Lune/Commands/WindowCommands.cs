using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;

using Lune.ViewModels;
using Lune.Views;

namespace Lune.Commands
{
    class WindowCommands : ICommand
    {
        TabControl _appTab;
        UserSettingsViewModel _usrVm;
        WindowViewModel _winVm;

        public WindowCommands(TabControl appTab, UserSettingsViewModel usrVm, WindowViewModel winVm)
        {
            _appTab = appTab;
            _usrVm = usrVm;
            _winVm = winVm;
        }
        #region
        public bool CanExecute(object parameter)
        {
            return true;
        }

        public void Execute(object sender)
        {
            switch((string)sender){
                case "Settings":
                    if (_appTab.Items.Count == 1)
                    {
                        v_settings vSettings = new v_settings();
                        vSettings.DataContext = _winVm;
                        v_LibrarySubsetting subset = new v_LibrarySubsetting();
                        subset.DataContext = _usrVm;

                        vSettings.pathsPanel.Children.Add(subset);
                        _appTab.Items.Add(vSettings);
                    }
                    _appTab.SelectedIndex = 1;
                    break;

                case "Back":
                    _appTab.SelectedIndex = 0;
                    break;
             }
        }

        public event EventHandler CanExecuteChanged
        {
            add { CommandManager.RequerySuggested += value; }
            remove { CommandManager.RequerySuggested -= value; }
        }
        #endregion
    }
}
