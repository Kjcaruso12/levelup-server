# Generated by Django 4.0.4 on 2022-04-18 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0004_alter_game_gamer_alter_game_gametype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.game'),
        ),
    ]