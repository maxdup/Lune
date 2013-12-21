using System;
using System.Collections.Generic;
using System.Collections.Specialized;
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

namespace Lune.Views
{
    /// <summary>
    /// Interaction logic for v_LibrarySubsetting.xaml
    /// </summary>
    public partial class v_LibrarySubsetting : UserControl
    {
        StringCollection paths;
        public v_LibrarySubsetting()
        {
            if (Properties.Settings.Default.LibraryPaths != null)
                paths = Properties.Settings.Default.LibraryPaths;
            else
                paths = new StringCollection() { "none"};
            InitializeComponent();
        }
        public void DeletePath(object sender, RoutedEventArgs e)
        {
            Properties.Settings.Default.LibraryPaths.Remove((string)((Button)sender).DataContext); //holy macaroni
            Properties.Settings.Default.Save();
            this.listPaths.Items.Refresh();
        }
    }
}
