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
        Panel MainPanel;
        UIElement[] UIonHold;

        public WindowCommands(Panel MainPanel)
        {
            this.MainPanel = MainPanel;
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
                    UIonHold = new UIElement[MainPanel.Children.Count];
                    MainPanel.Children.CopyTo(UIonHold,0);
                    v_LibrarySubsetting libsubset = new v_LibrarySubsetting();
                    UserSettingsViewModel uSettingVM = new UserSettingsViewModel(libsubset);
                    libsubset.DataContext = uSettingVM;
                    MainPanel.Children.Clear();
                    MainPanel.Children.Add(libsubset);
                    break;
                case "Back":
                    if (UIonHold != null){
                        MainPanel.Children.Clear();
                        foreach (UIElement ele in UIonHold)
                        {
                            MainPanel.Children.Add(ele);
                        }
                        UIonHold = null;
                    }
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
