# Generated by Django 5.0.6 on 2024-10-01 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='homepage',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
