# Generated by Django 5.0.6 on 2024-07-28 20:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0006_alter_team_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="name",
            field=models.CharField(
                choices=[
                    ("African Stars FC", "African Stars FC"),
                    ("Blue Waters FC", "Blue Waters FC"),
                    ("Civics FC", "Civics FC"),
                    ("Eshoke Chula Chula FC", "Eshoke Chula Chula FC"),
                    ("Khomas Nampol FC", "Khomas Nampol FC"),
                    ("KK Palace FC", "KK Palace FC"),
                    ("Mighty Gunners fC", "Mighty Gunners FC"),
                    (
                        "Namibia Collection Services FC",
                        "Namibia Collection Services FC",
                    ),
                    ("Okahandja United FC", "Okahandja United FC"),
                    ("Ongos FC", "Ongos FC"),
                    ("Tigers FC", "Tigers FC"),
                    ("Young African FC", "Young African FC"),
                    ("Young Brazilians FC", "Young Brazilians FC"),
                ],
                max_length=100,
                unique=True,
            ),
        ),
    ]
