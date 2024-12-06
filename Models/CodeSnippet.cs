namespace FamousTechCollabApp.Models
{
    public class CodeSnippet
    {
        public int Id { get; set; }
        public string Code { get; set; }
        public string Language { get; set; }
        public int ProjectId { get; set; }
        public Project Project { get; set; }
        public int UserId { get; set; }
        public User User { get; set; }
    }
}

