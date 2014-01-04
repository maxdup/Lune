using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;
using System.Collections.Specialized;
using System.IO;
using System.Windows.Controls;

using Lune.Views;
using Lune.ViewModels;
using System.Windows.Forms;

namespace Lune.Commands
{
    //this class is kinda gettho
    class SettingsCommands : ICommand
    {
        private UserSettingsViewModel _vmSettings;

        public SettingsCommands( UserSettingsViewModel vm)
        {
            _vmSettings = vm;//probably remove?
        }
        #region ICommand Members

        public bool CanExecute(object parameter)
        {
            return true;
        }

        public void Execute(object sender)
        {

            if (sender is System.Windows.Controls.ListBoxItem)
            {
                sender = ((System.Windows.Controls.ListBoxItem)sender).Content;
            }
            
            switch ((string)sender)
            {
                
                case "AddDir":
                    FolderBrowserDialog dialog = new FolderBrowserDialog();
                    dialog.ShowDialog();
                    //validating the path
                    if (dialog.SelectedPath != "" && Directory.Exists(dialog.SelectedPath))
                    {
                        bool subpath = false;
                        List<string> remove = new List<string>();

                        foreach (String path in Properties.Settings.Default.LibraryPaths)//checks path validity
                        {
                            if (dialog.SelectedPath.StartsWith(path))
                            {
                                subpath = true;
                                //todo: add message "path x is subpath of already contained in path y, not adding"
                                break;
                            }
                            if (path.StartsWith(dialog.SelectedPath))
                            {
                                remove.Add(path); //lists paths made redundant
                            }
                        }

                        if (!subpath)
                        {
                            if (remove.Count == 0)
                            {
                                //todo: add message "paths xyz have been made redundant and will be removed ok/cancel"
                                foreach (String path in remove)//removes paths made redundant
                                {
                                    Properties.Settings.Default.LibraryPaths.Remove(path);
                                }
                            }
                            _vmSettings.paths.Add(dialog.SelectedPath);
                            Properties.Settings.Default.LibraryPaths.Add(dialog.SelectedPath);
                            Properties.Settings.Default.Save();
                        }
                    }
                    break;
                default:
                    _vmSettings.paths.Remove((string)sender);
                    Properties.Settings.Default.LibraryPaths.Remove((string)sender);
                    Properties.Settings.Default.Save();
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
