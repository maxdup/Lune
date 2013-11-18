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
            LibVm = new LibraryViewModel(player, libraryDisplay);
            PlayVm = new PlaybackViewModel(player);

            InitViews();

            Database bae = new Database();//dunno what to make of this yet
        }

        private void InitViews()
        {
            v_ViewControls viewControls = new v_ViewControls();
            viewControls.DataContext = LibVm;
            ViewsDisplay.Children.Add(viewControls);

            v_playbackStatus playbackStatus = new v_playbackStatus();
            playbackStatus.DataContext = PlayVm.getPlayer();
            StatusDisplay.Children.Add(playbackStatus);

            v_mediaControls mediaControls = new v_mediaControls();
            mediaControls.DataContext = PlayVm;
            ControlsDisplay.Children.Add(mediaControls);

            libraryDisplay.Children.Add(new v_songs()); // not going to cut it
        }

        //Everything down are window controls, resize, close, minimize etc...  (move to new viwemodel?)
        private void TriggerMoveWindow(object sender, MouseEventArgs e)
        {
            if (e.LeftButton == MouseButtonState.Pressed)
            {
                if (WindowState == System.Windows.WindowState.Maximized)
                {
                    WindowState = System.Windows.WindowState.Normal;

                    double pct = PointToScreen(e.GetPosition(this)).X / System.Windows.SystemParameters.PrimaryScreenWidth;
                    Top = 0;
                    Left = e.GetPosition(this).X - (pct * Width);
                }
                DragMove();
            }
        }

        private void TriggerMaximize(object sender, MouseButtonEventArgs e)
        {
            if (WindowState == System.Windows.WindowState.Maximized)
                WindowState = System.Windows.WindowState.Normal;
            else if (WindowState == System.Windows.WindowState.Normal)
                WindowState = System.Windows.WindowState.Maximized;
        }
        private void TriggerMinimize(object sender, RoutedEventArgs e)
        {
            WindowState = System.Windows.WindowState.Minimized;
        }
        private void TriggerClose(object sender, RoutedEventArgs e)
        {
            Close();
        }
    }
}
