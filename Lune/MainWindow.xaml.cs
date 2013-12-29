using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

using Lune.Views;
using Lune.ViewModels;

namespace Lune
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        Player player;

        PlaybackViewModel PlayVm;
        LibraryViewModel LibVm;

        public MainWindow()
        {
            InitializeComponent();
            
            player = new Player();
            
            LibVm = new LibraryViewModel(player, MainPanel);
            PlayVm = new PlaybackViewModel(player);

            InitViews();
            if (Properties.Settings.Default.LibraryPaths == null)
            {
                //call a welcome screen (first time use)
                Properties.Settings.Default.LibraryPaths = new System.Collections.Specialized.StringCollection();
            }

            Database bae = new Database();//dunno what to make of this yet
        }

        private void InitViews()
        {
            v_topBar topBar = new v_topBar();
            v_bottomBar bottomBar = new v_bottomBar();

            v_ViewControls viewControls = new v_ViewControls();
            viewControls.DataContext = LibVm;
            bottomBar.ViewsDisplay.Children.Add(viewControls);

            v_playbackStatus playbackStatus = new v_playbackStatus();
            playbackStatus.DataContext = PlayVm.getPlayer();
            bottomBar.StatusDisplay.Children.Add(playbackStatus);

            v_mediaControls mediaControls = new v_mediaControls();
            mediaControls.DataContext = PlayVm.getPlayer();
            bottomBar.ControlsDisplay.Children.Add(mediaControls);

            topBarDisplay.Children.Add(topBar);
            LibVm.libViews.Execute("Artists"); //todo: make this a user setting eventually (prefered welcome screen)
            bottomBarDisplay.Children.Add(bottomBar);
        }
    }
}
