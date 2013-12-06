using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;
using System.Windows.Forms;
using Lune.Views;

namespace Lune.Commands
{
    class SettingsCommands : ICommand
    {
        v_LibrarySubsetting _pathView;
        public SettingsCommands(v_LibrarySubsetting pathView)
        {
            _pathView = pathView;
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
