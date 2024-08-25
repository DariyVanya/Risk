using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace _1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_Validated(object sender, EventArgs e)
        {

        }

        private List<int> get_coef() {
            List<int> st_coef = new List<int>();
            if (verybad_txt.Text == "" || bad_txt.Text == "" || good_txt.Text == "" || perfect_txt.Text == "")
            {
                MessageBox.Show("Заповніть всі поля таблиць");
                return st_coef;
            }
            st_coef.Add(Convert.ToInt32(verybad_txt.Text));
            st_coef.Add(Convert.ToInt32(bad_txt.Text));
            st_coef.Add(Convert.ToInt32(good_txt.Text));
            st_coef.Add(Convert.ToInt32(perfect_txt.Text));

            List<int> coef = new List<int>();
            if (rainhouse_cmbbox.SelectedIndex == -1 || dryhouse_cmbbox.SelectedIndex == -1 || rainyforest_cmbbox.SelectedIndex == -1 || dryforest_cmbbox.SelectedIndex == -1)
            {
                MessageBox.Show("Заповніть всі поля таблиць");
                return coef;
            }
            coef.Add(st_coef[rainhouse_cmbbox.SelectedIndex]);
            coef.Add(st_coef[dryhouse_cmbbox.SelectedIndex]);
            coef.Add(st_coef[rainyforest_cmbbox.SelectedIndex]);
            coef.Add(st_coef[dryforest_cmbbox.SelectedIndex]);

            return coef;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            List<int> a = get_coef();

            double house = Convert.ToDouble(rain_txt.Text) * a[0] + (1 - Convert.ToDouble(rain_txt.Text)) * a[1];
            double forest = Convert.ToDouble(rain_txt.Text) * a[2] + (1 - Convert.ToDouble(rain_txt.Text)) * a[3];

            res_house_lbl.Text = "Дім:"+house.ToString();
            res_forest_lbl.Text = "Ліс:"+forest.ToString();

            if (house > forest)
            {
                res_lbl.Text = "Сидимо дома.";
            } else
            {
                res_lbl.Text = "Ну ліс так ліс.";
            }
            
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
