﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinFormsApp2
{
    public partial class Kis_Lastikleri : Form
    {
        public Kis_Lastikleri()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            sayfa2 sayfa2 = new sayfa2();
            this.Hide();
            sayfa2.ShowDialog();
        }
    }
}
