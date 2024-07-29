from django.db import models

class Team(models.Model):
    TEAM_CHOICES = [
        ("African Stars FC", "African Stars FC"),
        ("Blue Waters FC", "Blue Waters FC"),
        ("Civics FC", "Civics FC"),
        ("Eshoke Chula Chula FC", "Eshoke Chula Chula FC"),
        ("Khomas Nampol FC", "Khomas Nampol FC"),
        ("KK Palace FC", "KK Palace FC"),
        ("Mighty Gunners fC", "Mighty Gunners FC"),
        ("Namibia Collection Services FC", "Namibia Collection Services FC"),
        ("Okahandja United FC", "Okahandja United FC"),
        ("Ongos FC", "Ongos FC"),
        ("Tigers FC", "Tigers FC"),
        ("Young African FC", "Young African FC"),
        ("Young Brazilians FC", "Young Brazilians FC"),
    ]

    name = models.CharField(max_length=100, choices=TEAM_CHOICES, unique=True)
    logo = models.ImageField(upload_to='team_logos/')

    def __str__(self):
        return self.name

class Fixture(models.Model):
    home = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_fixtures')
    away = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_fixtures')
    date = models.DateField(auto_now_add=False)
    time = models.TimeField(auto_now_add=False)
    stadium = models.CharField(max_length=100, blank=False, null=False)
    town = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self):
        return f"{self.home} vs {self.away} on {self.date} at {self.time}"
    class Meta:
        ordering = ["-date"]

class Result(models.Model):
    fixture = models.OneToOneField(Fixture, on_delete=models.CASCADE)
    home_score = models.PositiveIntegerField()
    away_score = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=False)
    
    def __str__(self):
        return f"{self.fixture.home} {self.home_score} - {self.away_score} {self.fixture.away}"

    @property
    def home_team(self):
        return self.fixture.home

    @property
    def away_team(self):
        return self.fixture.away
    
    class Meta:
        ordering = ["-date"]

class Story(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    image = models.ImageField(upload_to="home/upload", blank=False, null=False)
    
    def __str__(self):
        return self.title
class News(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to="home/news", blank=False, null=False)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} on {self.date.strftime('%Y-%m-%d')}"
class Tv(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to="home/news", blank=False, null=False)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} on the {self.date}"
class CAF(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to="home/news", blank=False, null=False)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} on {self.date.strftime('%Y-%m-%d')}"
class Premiership(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to="home/news", blank=False, null=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} on {self.date.strftime('%Y-%m-%d')}"
class NFACup(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to="home/news", blank=False, null=False)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} on {self.date.strftime('%Y-%m-%d')}"
