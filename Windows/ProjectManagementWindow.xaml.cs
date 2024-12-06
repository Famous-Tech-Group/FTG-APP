using System.Linq;
using System.Windows;
using FamousTechCollabApp.Data;
using FamousTechCollabApp.Models;

namespace FamousTechCollabApp.Windows
{
    public partial class ProjectManagementWindow : Window
    {
        private readonly User _currentUser;

        public ProjectManagementWindow(User currentUser)
        {
            InitializeComponent();
            _currentUser = currentUser;
            LoadProjects();
        }

        private void LoadProjects()
        {
            using (var context = new AppDbContext())
            {
                var projects = context.Projects.Where(p => p.OwnerId == _currentUser.Id).ToList();
                ProjectsListBox.ItemsSource = projects;
            }
        }

        private void AddProjectButton_Click(object sender, RoutedEventArgs e)
        {
            using (var context = new AppDbContext())
            {
                var newProject = new Project
                {
                    Name = ProjectNameTextBox.Text,
                    OwnerId = _currentUser.Id
                };
                context.Projects.Add(newProject);
                context.SaveChanges();
                LoadProjects();
            }
        }
    }
}
