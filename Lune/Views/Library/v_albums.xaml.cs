using Lune.ViewModels;
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

namespace Lune.Views
{

    public partial class v_albums : UserControl
    {
        private LibraryViewModel vm { get { return DataContext as LibraryViewModel; } }

        public v_albums()
        {
            InitializeComponent();
        }
        private void AlbumSelection(object sender, RoutedEventArgs e)
        {
            if (listB_Albums.SelectedValue != null)
            {
                vm.albumFilter(listB_Albums.SelectedValue.ToString());
            }
        }
    }
}
