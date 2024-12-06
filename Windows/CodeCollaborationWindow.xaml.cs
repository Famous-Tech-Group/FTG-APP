using System.Windows;
using FamousTechCollabApp.Models;

namespace FamousTechCollabApp.Windows
{
    public partial class CodeCollaborationWindow : Window
    {
        private readonly Project _currentProject;

        public CodeCollaborationWindow(Project project)
        {
            InitializeComponent();
            _currentProject = project;
        }

        private void SaveSnippetButton_Click(object sender, RoutedEventArgs e)
        {
            using (var context = new AppDbContext())
            {
                var snippet = new CodeSnippet
                {
                    Code = CodeTextBox.Text,
                    Language = LanguageComboBox.Text,
                    ProjectId = _currentProject.Id
                };
                context.CodeSnippets.Add(snippet);
                context.SaveChanges();
                MessageBox.Show("Snippet saved!");
            }
        }
    }
}
