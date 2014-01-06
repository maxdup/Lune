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
        private LibraryViewModel _vmLibrary;

        public SettingsCommands( UserSettingsViewModel UserVm, LibraryViewModel Libvm)
        {
            _vmSettings = UserVm;
            _vmLibrary = Libvm;
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
                    addPath(dialog.SelectedPath);
                    break;
                default: //assumes we are looking to delete a path
                    _vmLibrary.lib.GetSongs().RemoveAll(r=> r.path.StartsWith((string)sender));
                    _vmSettings.paths.Remove((string)sender);
                    Properties.Settings.Default.LibraryPaths.Remove((string)sender);
                    Properties.Settings.Default.Save();
                    break;
            }
        }

        private void addPath(string AddedDir)
        {
            if (AddedDir != "" && Directory.Exists(AddedDir))
            {
                bool subpath = false;
                List<string> remove = new List<string>();

                foreach (String path in Properties.Settings.Default.LibraryPaths)//checks path validity
                {
                    if (AddedDir.StartsWith(path))
                    {
                        subpath = true;
                        //todo: add message "path x is subpath of already contained in path y, not adding"
                        break;
                    }
                    if (path.StartsWith(AddedDir))
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
                    MediaFiles searcher = new MediaFiles(_vmLibrary.lib);
                    searcher.scrapper(AddedDir);
                    _vmLibrary.PropertyChange("songsDisplayed");
                    _vmLibrary.PropertyChange("albumsDisplayed");
                    _vmLibrary.PropertyChange("artistDisplayed");
                    _vmSettings.paths.Add(AddedDir);
                    Properties.Settings.Default.LibraryPaths.Add(AddedDir);
                    Properties.Settings.Default.Save();
                }
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
