from django.db import models

class Game(models.Model):
    gametype = models.ForeignKey("gametype", on_delete=models.CASCADE)
    title = models.CharField(max_length=55)
    maker = models.CharField(max_length=55)
    gamer = models.ForeignKey("gamer", on_delete=models.CASCADE)
    number_of_players = models.IntegerField(default=None)
    skill_level = models.IntegerField(default=None)