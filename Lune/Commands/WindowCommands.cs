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
        UserSettingsViewModel _vm;

        public WindowCommands(Panel MainPanel, UserSettingsViewModel vm)
        {
            this.MainPanel = MainPanel;
            _vm = vm;
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
                    if (UIonHold == null)
                    {
                        UIonHold = new UIElement[MainPanel.Children.Count];
                        MainPanel.Children.CopyTo(UIonHold, 0);
                    }

                    v_settings vSettings = new v_settings();
                    
                    vSettings.DataContext = _vm;

                    MainPanel.Children.Clear();
                    MainPanel.Children.Add(vSettings);
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
