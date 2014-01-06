using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;

using Lune.Commands;
using System.Windows.Controls;

namespace Lune.ViewModels
{
    class WindowViewModel
    {
        public ICommand windowCtrls { get; private set; }
        public Panel MainPanel { get; private set; }//remove or keep for later use
        public WindowViewModel(Panel panel, UserSettingsViewModel vm)
        {
            MainPanel = panel;
            windowCtrls = new WindowCommands(panel, vm);
        }
    }
}
