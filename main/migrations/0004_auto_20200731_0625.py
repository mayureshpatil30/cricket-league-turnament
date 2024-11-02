# Generated by Django 2.2.14 on 2020-07-31 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_matches_points'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matches',
            options={'verbose_name_plural': 'Matches'},
        ),
        migrations.AlterModelOptions(
            name='points',
            options={'verbose_name_plural': 'Points'},
        ),
        migrations.AlterField(
            model_name='matches',
            name='winner_team',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=2),
        ),
    ]