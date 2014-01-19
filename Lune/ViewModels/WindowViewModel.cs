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
        public UserSettingsViewModel usrVm {get; private set;}
        public ICommand windowCtrls { get; private set; }
        public WindowViewModel(TabControl appTab, UserSettingsViewModel vm)
        {
            windowCtrls = new WindowCommands(appTab, vm, this);
            usrVm = vm;
        }
    }
}
