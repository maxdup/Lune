using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;

using Lune.ViewModels;
using System.Diagnostics;
using System.Windows.Controls;


namespace Lune.Commands
{
    internal class PlaybackCommands : ICommand
    {
        private Player _player;

        public PlaybackCommands(Player player)
        {
            _player = player;
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
                case "skip":
                    _player.Skip();
                    break;
                case "hybrid":
                    _player.Hybrid();
                    break;
                case "stop":
                    _player.Stop();
                    break;
                case "prev":
                    _player.Prev();
                    break;
            }
        }

        public event EventHandler CanExecuteChanged
        {
            add { CommandManager.RequerySuggested += value; }
            remove {CommandManager.RequerySuggested -= value; }
        }

        #endregion
    }
}
