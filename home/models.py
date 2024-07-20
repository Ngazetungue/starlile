from django.db import models

# FIXTURES, RESULTS MODELS START
class Team(models.Model):
    TEAM_CHOICES = [
        ("African Stars FC", "African Stars FC"),
        ("Blue Waters FC", "Blue Waters FC"),
        ("Civics FC", "Civics FC"),
        ("Eshoke Chula Chula FC", "Eshoke Chula Chula FC"),
        ("Khomas Nampol FC", "Khomas Nampol FC"),
        ("KK Palace FC", "KK Palace FC"),
        ("Okahandja United FC", "Okahandja United FC"),
        ("Ongos FC", "Ongos FC"),
        ("Tigers FC", "Tigers FC"),
        ("Young African FC", "Young African FC"),
        ("Young Brazilians FC", "Young Brazilians FC"),
    ]

    name = models.CharField(max_length=100, choices=TEAM_CHOICES, unique=True)

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

class Result(models.Model):
    fixture = models.OneToOneField(Fixture, on_delete=models.CASCADE)
    home_score = models.PositiveIntegerField()
    away_score = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.fixture.home} {self.home_score} - {self.away_score} {self.fixture.away}"

    @property
    def home_team(self):
        return self.fixture.home

    @property
    def away_team(self):
        return self.fixture.away

# FIXTURES, RESULTS MODELS END