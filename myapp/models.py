from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100)
    open_time = models.TimeField()
    close_time = models.TimeField()
    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=5)
    join_time = models.DateTimeField(auto_now_add=True)
    number_of_matches = models.IntegerField(default=0)
    number_of_shuttlecock = models.IntegerField(default=0)

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name='players'
    )

    def __str__(self):
        return self.name