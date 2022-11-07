using System;
using System.Collections.Generic;
using System.Diagnostics;
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
    /// Block.xaml에 대한 상호 작용 논리
    /// </summary>
    public partial class Block : UserControl
    {
        public int State = 1;

        public Block()
        {
            InitializeComponent();
        }

        private void UserControl_MouseDown(object sender, MouseButtonEventArgs e)
        {
            Color bgcolor = Color.FromRgb(255, 255, 255);
            State = (State + 1) % 2;
            if (State == 1)
            {
                bgcolor = Color.FromRgb(239, 100, 100);
            }
            displayState.Fill = new SolidColorBrush(bgcolor);
        }
    }
}
