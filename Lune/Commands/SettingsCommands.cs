using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;
using System.Windows.Forms;

using System.Collections.Specialized;
using Lune.Views;
using Lune.ViewModels;

namespace Lune.Commands
{
    class SettingsCommands : ICommand
    {
        v_LibrarySubsetting _pathView;
        UserSettingsViewModel _vmSettings;
        public SettingsCommands(v_LibrarySubsetting pathView, UserSettingsViewModel vm)
        {
            _pathView = pathView;
            _vmSettings = vm;
        }
        #region ICommand Members

        public bool CanExecute(object parameter)
        {
            return true;
        }

        public void Execute(object sender)
        {
            
            switch ((string)sender)
            {                
                case "AddDir":
                    FolderBrowserDialog dialog = new FolderBrowserDialog();
                    dialog.ShowDialog();

                    Properties.Settings.Default.LibraryPaths.Add(dialog.SelectedPath);
                    
                    Properties.Settings.Default.Save();
                    _pathView.listPaths.Items.Refresh();
                    break;
                /* It's probably impossible to remove paths from here, paths will be removed from the view's code behind for now.
                 * Having the sender be a parameter string is kinda problematic
                case "DeletePath":
                    ((StringCollection)_pathView.listPaths.ItemsSource).RemoveAt(0); //yeah.....
                    
                    Properties.Settings.Default.Save();
                    _pathView.listPaths.Items.Refresh();
                    break;
                 */
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
