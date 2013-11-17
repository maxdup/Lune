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
            LibVm = new LibraryViewModel(player);
            PlayVm = new PlaybackViewModel(player);

            InitViews();

            Database bae = new Database();//dunno what to make of this yet

            b_View_click(new Button(), null);
        }

        private void InitViews()
        {
            v_mediaControls mediaControls = new v_mediaControls();
            mediaControls.DataContext = PlayVm;
            ControlsDisplay.Children.Add(mediaControls);

            v_ViewControls viewControls= new v_ViewControls();
            viewControls.DataContext = LibVm;
            libraryDisplay.Children.Add(viewControls);
        }

        //event for player controls (play, pause, stop, skip...)
        private void b_media_click(object sender, RoutedEventArgs e)
        {
            switch (((Button)sender).Name)
            {
                case "b_skip":
                    player.Skip();
                    break;
                case "b_hybrid":
                    player.Hybrid();
                    break;
                case "b_stop":
                    player.Stop();
                    break;
                case "b_prev":
                    player.Prev();
                    break;
            }
        }

        //selects from different view to display the music Library
        private void b_View_click(object sender, RoutedEventArgs e)
        {
            libraryDisplay.Children.Clear();
            switch (((Button)sender).Name)
            {
                case "vAlbum":
                    libraryDisplay.Children.Add(new v_albums());
                    break;
                case "vSong":
                    v_songs songs = new v_songs();
                    songs.getListBox().ItemsSource = LibVm.getSongsDisplayed();
                    songs.DataContext = LibVm;
                    libraryDisplay.Children.Add(songs);
                    break;
                default:
                    libraryDisplay.Children.Add(new v_artists());
                    break;
            }
        }

        //Everything down are window controls, resize, close, minimize etc...
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
