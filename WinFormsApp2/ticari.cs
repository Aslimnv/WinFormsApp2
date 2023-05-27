using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace WinFormsApp2
{
    public partial class ticari : Form
    {
        public ticari()
        {
            InitializeComponent();

            comboBox1.Items.Add("205/55R16 91V (1.752,06 TL)");
            comboBox1.Items.Add("185/65R15 88T (1.523,51 TL)");
            comboBox1.Items.Add("245/35R20 95Y XL (3.901,79 TL)");
            comboBox1.Items.Add("195/65R15 91H (1.404,00 TL)");
            comboBox1.Items.Add("275/40R18 99Y (6.246,44 TL)");
            comboBox1.Items.Add("245/40R18 97Y XL (3.460,41 TL)");
            comboBox1.Items.Add("255/40R18 99Y XL (5.374,49 TL)");
            comboBox1.Items.Add("245/45R18 100Y XL (3.360,46 TL)");

            comboBox2.Items.Add("205/55R16 91V (1.193,40 TL)");
            comboBox2.Items.Add("185/65R15 88H (1.093,64 TL)");
            comboBox2.Items.Add("185/65R14 86H (994,08 TL)");
            comboBox2.Items.Add("195/65R15 91V (1.041,00 TL)");
            comboBox2.Items.Add("175/65R14 82H (984,00 TL)");
            comboBox2.Items.Add("225/45R17 94W XL (1.299,07 TL)");
            comboBox2.Items.Add("195/55R16 91V XL (1.584,54 TL)");
            comboBox2.Items.Add("235/45R18 98Y XL (2.556,60 TL)");

            comboBox3.Items.Add("205/55R16 91V (1.367,00 TL)");
            comboBox3.Items.Add("195/65R15 91H (1.110,56 TL)");
            comboBox3.Items.Add("175/65R14 82T (919,52 TL)");
            comboBox3.Items.Add("185/65R15 88H (1.216,80 TL)");
            comboBox3.Items.Add("185/65R14 86T (1.045,49 TL)");
            comboBox3.Items.Add("225/45R17 91W (1.352,83 TL)");
            comboBox3.Items.Add("215/50R17 95W XL (2.046,32 TL)");
            comboBox3.Items.Add("215/55R16 93V (1.917,98 TL)");

            comboBox4.Items.Add("205/55R16 91V (1.277,40 TL)");
            comboBox4.Items.Add("195/55R16 87V (1.356,06 TL)");
            comboBox4.Items.Add("175/65R14 82T (1.063,52 TL)");
            comboBox4.Items.Add("195/50R15 82V (1.188,06 TL)");
            comboBox4.Items.Add("215/55R17 94W (2.102,32 TL)");
            comboBox4.Items.Add("205/60R16 92H (1.670,78 TL)");
            comboBox4.Items.Add("185/60R15 84T (1.184,48 TL)");
            comboBox4.Items.Add("215/50R17 95V XL (2.477,52 TL)");

            comboBox5.Items.Add("205/55R16 91V (1.535,00 TL)");
            comboBox5.Items.Add("185/65R15 88H (1.299,09 TL)");
            comboBox5.Items.Add("205/55R16 91H (1.534,88 TL)");
            comboBox5.Items.Add("195/65R15 91V (1.208,00 TL)");
            comboBox5.Items.Add("235/45R18 98Y XL (3.089,72 TL)");
            comboBox5.Items.Add("225/55R17 97H (2.783,80 TL)");
            comboBox5.Items.Add("215/65R16 98H (1.754,70 TL)");
            comboBox5.Items.Add("245/45R18 100Y XL (3.292,41 TL)");

            comboBox6.Items.Add("175/70R13 82T (775,67 TL)");
            comboBox6.Items.Add("205/55R16 91H (1.064,59 TL)");
            comboBox6.Items.Add("185/65R14 86T (910,08 TL)");
            comboBox6.Items.Add("175/65R14 82T (894,40 TL)");
            comboBox6.Items.Add("165/80R13 83T (776,78 TL)");
            comboBox6.Items.Add("185/60R15 84H (878,08 TL)");
            comboBox6.Items.Add("215/55R17 98W XL (1.444,93 TL)");
            comboBox6.Items.Add("225/45R17 94W XL (1.230,75 TL)");


        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = Image.FromFile("C:\\Users\\Aslış\\Desktop\\lastik");
        }

        private void pictureBox2_Click(object sender, EventArgs e)
        {
            pictureBox2.Image = Image.FromFile("C:\\Users\\Aslış\\Desktop\\lastik");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            sayfa2 sayfa2 = new sayfa2();
            this.Hide();
            sayfa2.ShowDialog();
        }

        private void ticari_Load(object sender, EventArgs e)
        {

        }
    }
}
