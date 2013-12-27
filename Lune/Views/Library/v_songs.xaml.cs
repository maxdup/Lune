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
    /// Interaction logic for v_songs.xaml
    /// </summary>
    public partial class v_songs : UserControl
    {
        private LibraryViewModel vm { get { return DataContext as LibraryViewModel; } }

        public v_songs()
        {
            InitializeComponent();
        }
        public ListBox getListBox()
        {
            return listB_Songs;
        }
        public void sendListForPlay(object sender, RoutedEventArgs e)//consider refactoring
        {
            vm.Play(sender);
        }
    }
}
