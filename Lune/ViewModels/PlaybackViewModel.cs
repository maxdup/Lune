using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;

using Lune;
using Lune.Commands;


namespace Lune.ViewModels
{
    class PlaybackViewModel
    {
        Player player;
        public ICommand ctrls { get; private set; }
        public string songinfo { get { return player.currSongInfo; }  set {player.currSongInfo = value; } }

        public PlaybackViewModel(Player player)
        {
            this.player = player;
            ctrls = new PlaybackCommands(player);
        }
        public Player getPlayer()
        {
            return player;
        }
    }
}
