using System;
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
    public partial class sayfa2 : Form
    {
        public sayfa2()
        {
            InitializeComponent();
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = Image.FromFile("C:\\Users\\Aslış\\Desktop\\logo");
        }

        private void pictureBox2_Click(object sender, EventArgs e)
        {
            pictureBox2.Image = Image.FromFile("C:\\Users\\Aslış\\Desktop\\Otomobil");
        }

        private void pictureBox3_Click(object sender, EventArgs e)
        {
            pictureBox3.Image = Image.FromFile("C:\\Users\\Aslış\\Desktop\\araba");
        }

        private void pictureBox4_Click(object sender, EventArgs e)
        {
            pictureBox4.Image = Image.FromFile("C:\\Users\\Aslış\\Desktop\\ticari");
        }

        private void pictureBox5_Click(object sender, EventArgs e)
        {
            pictureBox5.Image = Image.FromFile("C:\\Users\\Aslış\\Desktop\\otobüs");
        }

        private void pictureBox6_Click(object sender, EventArgs e)
        {
            pictureBox6.Image = Image.FromFile("C:\\Users\\Aslış\\Desktop\\motor");
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {


        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (radioButton1.Checked)
            {
                araba araba = new araba();
                this.Hide();
                araba.ShowDialog();

            }
            else if (radioButton2.Checked)
            {
                suv suv = new suv();
                this.Hide();
                suv.ShowDialog();

            }
            else if (radioButton3.Checked)
            {
                ticari ticari = new ticari();
                this.Hide();
                ticari.ShowDialog();
            }
            else if (radioButton4.Checked)
            {
                Otobüs_Kamyon otobüs_Kamyon = new Otobüs_Kamyon();
                this.Hide();
                otobüs_Kamyon.ShowDialog();
            }
            else if (radioButton5.Checked)
            {
                Motosiklet motosiklet = new Motosiklet();
                this.Hide();
                motosiklet.ShowDialog();
            }
            else if (radioButton6.Checked)
            {
                is_makinesi is_makinesi = new is_makinesi();
                this.Hide();
                is_makinesi.ShowDialog();
            }
            else if (radioButton7.Checked)
            {
                Yaz_Lastileri yaz_Lastileri = new Yaz_Lastileri();
                this.Hide();
                yaz_Lastileri.ShowDialog();
            }
            else if (radioButton8.Checked)
            {
                Kis_Lastikleri kis_Lastikleri = new Kis_Lastikleri();
                this.Hide();
                kis_Lastikleri.ShowDialog();
            }
            else if (radioButton9.Checked)
            {
                _4Mevsimlik _4Mevsimlik = new _4Mevsimlik();
                this.Hide();
                _4Mevsimlik.ShowDialog();
            }
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void pictureBox7_Click(object sender, EventArgs e)
        {
            pictureBox7.Image = Image.FromFile("C:\\Users\\Aslış\\Desktop\\işmakinesi");
        }

        private void pictureBox8_Click(object sender, EventArgs e)
        {
            pictureBox8.Image = Image.FromFile("C:\\Users\\Aslış\\Desktop\\lastik");
        }

        private void pictureBox9_Click(object sender, EventArgs e)
        {
            pictureBox9.Image = Image.FromFile("C:\\Users\\Aslış\\Desktop\\sun");
        }

        private void pictureBox10_Click(object sender, EventArgs e)
        {
            pictureBox10.Image = Image.FromFile("C:\\Users\\Aslış\\Desktop\\kar");
        }

        private void radioButton4_CheckedChanged(object sender, EventArgs e)
        {

        }
    }
}
