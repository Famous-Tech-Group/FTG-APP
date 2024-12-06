using System;
using System.Linq;
using System.Windows;
using System.Windows.Threading;
using FamousTechCollabApp.Data;
using FamousTechCollabApp.Models;

namespace FamousTechCollabApp.Windows
{
    public partial class EphemeralChatWindow : Window
    {
        private readonly Project _currentProject;

        public EphemeralChatWindow(Project project)
        {
            InitializeComponent();
            _currentProject = project;
            LoadMessages();
        }

        private void LoadMessages()
        {
            using (var context = new AppDbContext())
            {
                var messages = context.ChatMessages
                    .Where(m => m.ProjectId == _currentProject.Id && m.Timestamp > DateTime.Now.AddMinutes(-5))
                    .OrderByDescending(m => m.Timestamp)
                    .ToList();

                ChatListBox.ItemsSource = messages.Select(m => $"{m.Timestamp:HH:mm} - {m.MessageText}");
            }

            StartMessageCleanupTimer();
        }

        private void StartMessageCleanupTimer()
        {
            DispatcherTimer timer = new DispatcherTimer
            {
                Interval = TimeSpan.FromMinutes(1)
            };
            timer.Tick += (s, e) =>
            {
                using (var context = new AppDbContext())
                {
                    var oldMessages = context.ChatMessages
                        .Where(m => m.Timestamp <= DateTime.Now.AddMinutes(-5))
                        .ToList();
                    context.ChatMessages.RemoveRange(oldMessages);
                    context.SaveChanges();
                }
                LoadMessages();
            };
            timer.Start();
        }

        private void SendMessageButton_Click(object sender, RoutedEventArgs e)
        {
            if (!string.IsNullOrWhiteSpace(MessageTextBox.Text))
            {
                using (var context = new AppDbContext())
                {
                    var message = new ChatMessage
                    {
                        MessageText = MessageTextBox.Text,
                        Timestamp = DateTime.Now,
                        IsEphemeral = true,
                        ProjectId = _currentProject.Id
                    };
                    context.ChatMessages.Add(message);
                    context.SaveChanges();
                }

                MessageTextBox.Clear();
                LoadMessages();
            }
        }
    }
}
