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
using Lune.ViewModels;

namespace Lune.Views
{
    /// <summary>
    /// Interaction logic for v_topBar.xaml
    /// 
    /// see if most of this class can be moved to windowCommands.cs
    /// 
    /// </summary>
    public partial class v_topBar : UserControl
    {
        Window window;
        UIElementCollection UIonHold;
        public v_topBar()
        {
            InitializeComponent();
        }

        private void TriggerMoveWindow(object sender, MouseEventArgs e)
        {
            if (window == null)
                getWindow();
            if (e.LeftButton == MouseButtonState.Pressed)
            {
                if (window.WindowState == System.Windows.WindowState.Maximized)
                {
                    window.WindowState = System.Windows.WindowState.Normal;

                    double pct = PointToScreen(e.GetPosition(this)).X / System.Windows.SystemParameters.PrimaryScreenWidth;
                    window.Top = 0;
                    window.Left = e.GetPosition(this).X - (pct * Width);
                }
                window.DragMove();
            }
        }
        private void TriggerMaximize(object sender, RoutedEventArgs e)
        {
            if (window == null)
                getWindow();
            if (window.WindowState == System.Windows.WindowState.Maximized)
                window.WindowState = System.Windows.WindowState.Normal;
            else if (window.WindowState == System.Windows.WindowState.Normal)
                window.WindowState = System.Windows.WindowState.Maximized;
        }
        private void TriggerMaximize(object sender, MouseEventArgs e)
        {
            if (window == null)
                getWindow();
            if (window.WindowState == System.Windows.WindowState.Maximized)
                window.WindowState = System.Windows.WindowState.Normal;
            else if (window.WindowState == System.Windows.WindowState.Normal)
                window.WindowState = System.Windows.WindowState.Maximized;
        }
        private void TriggerMinimize(object sender, RoutedEventArgs e)
        {
            if (window == null)
                getWindow();
            window.WindowState = System.Windows.WindowState.Minimized;
        }
        private void TriggerClose(object sender, RoutedEventArgs e)
        {
            if (window == null)
                getWindow();
            window.Close();
        }
        private void getWindow()
        {
            window = Window.GetWindow(this);
        }
    }
}
