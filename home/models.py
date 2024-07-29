from django.db import models
from django_countries.fields import CountryField
from datetime import date
class Team(models.Model):
    TEAM_CHOICES = [
        ("African Stars FC", "African Stars FC"),
        ("Blue Waters FC", "Blue Waters FC"),
        ("Civics FC", "Civics FC"),
        ("Eshoke Chula Chula FC", "Eshoke Chula Chula FC"),
        ("Khomas Nampol FC", "Khomas Nampol FC"),
        ("KK Palace FC", "KK Palace FC"),
        ("Mighty Gunners FC", "Mighty Gunners FC"),
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

    class Meta:
        ordering = ['name']
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

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
        unique_together = ['home', 'away', 'date', 'time']

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

class Player(models.Model):
    POSITION_CHOICES = [
        ('GK', 'Goalkeeper'),
        ('DEF', 'Defender'),
        ('MID', 'Midfielder'),
        ('FWD', 'Forward'),
    ]

    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    photo = models.ImageField(upload_to='player_photo/')
    country = CountryField(blank=False, null=False)
    position = models.CharField(max_length=3, choices=POSITION_CHOICES, blank=False, null=False)
    bio = models.TextField(blank=False, null=False)
    shirt_number = models.PositiveIntegerField(default=0, unique=True)
    joined = models.DateField(blank=False, null=False)
    debut = models.DateField(blank=True, null=True)
    appearances = models.PositiveIntegerField(default=0)
    goals = models.PositiveIntegerField(default=0)
    assist = models.PositiveIntegerField(default=0)
    clean_sheet = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
        
    @property
    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

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
