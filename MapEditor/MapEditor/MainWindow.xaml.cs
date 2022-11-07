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

namespace MapEditor
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        const int Size_X = 15;
        const int Size_Y = 15;
        Block[,] blocks = new Block[Size_X, Size_Y];

        public MainWindow()
        {
            InitializeComponent();

        }

        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            for(int y=0; y<Size_Y; y++)
            {
                for(int x=0; x<Size_X; x++)
                {
                    blocks[y, x] = new Block();
                    blocks[y, x].Width = 25;
                    blocks[y, x].Height = 25;
                    blocks[y, x].Margin = new Thickness(x * 25, y * 25, 0, 0);
                    TaskGrid.Children.Add(blocks[y, x]);
                }
            }
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            string result = "===========================\n";
            for (int y = 0; y < Size_Y; y++)
            {
                result += "[";
                for (int x = 0; x < Size_X; x++)
                {
                    if (x == Size_X - 1)
                    {
                        result += $"{blocks[y, x].State}";
                    }
                    else
                    {
                        result += $"{blocks[y, x].State}, ";
                    }
                }
                result += "],\n";
            }
            Console.WriteLine(result);
        }
    }
}
