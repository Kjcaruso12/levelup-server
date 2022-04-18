from django.db import models

class Event(models.Model):
    game = models.ForeignKey("game", on_delete=models.CASCADE )
    description = models.TextField(max_length=100)
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    organizer = models.ForeignKey("gamer", on_delete=models.CASCADE)