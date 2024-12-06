using Microsoft.EntityFrameworkCore;

namespace FamousTechCollabApp.Data
{
    public class AppDbContext : DbContext
    {
        public DbSet<User> Users { get; set; }
        public DbSet<Project> Projects { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseNpgsql("Host=ep-noisy-forest-a42ebqlz-pooler.us-east-1.aws.neon.tech;Database=neondb;Username=neondb_owner;Password=7H5fxkvBGbEI;SslMode=Require");
        }
    }
}
