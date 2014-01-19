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
    /// Interaction logic for v_artists.xaml
    /// </summary>
    public partial class v_artists : UserControl
    {
        private LibraryViewModel vm { get { return DataContext as LibraryViewModel; } }

        public v_artists()
        {
            InitializeComponent();
        }
        private void ArtistSelection(object sender, RoutedEventArgs e)
        {
            vm.artistFilter(listB_Artists.SelectedValue.ToString());
        }
        private void AlbumSelection(object sender, RoutedEventArgs e)
        {
            if (listB_Albums.SelectedValue != null)
            {
                vm.albumFilter(listB_Albums.SelectedValue.ToString());
            }
        }
        public void syncToLib()
        {
            listB_Albums.DisplayMemberPath = "";
            listB_Artists.DisplayMemberPath = "";
        }
    }
}
