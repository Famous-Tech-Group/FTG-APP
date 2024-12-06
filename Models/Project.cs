namespace FamousTechCollabApp.Models
{
    public class Project
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public int OwnerId { get; set; }
        public User Owner { get; set; }
    }
}
