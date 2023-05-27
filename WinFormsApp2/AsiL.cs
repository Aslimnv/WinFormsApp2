namespace WinFormsApp2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = Image.FromFile("C:\\Users\\Aslýþ\\Desktop\\logo");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            sayfa2 fr2 = new sayfa2();
            this.Hide();
            fr2.ShowDialog();
        }
    }
}