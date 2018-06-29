from django.db import models

class Leaque(models.Model):
    leaque_id = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    def __str__(self):
        return self.leaque_id
    class Meta:
        ordering = ['id']

class Week(models.Model):
    position = models.CharField(max_length=20)
    leaque = models.ForeignKey('Leaque')
    def __str__(self):
        return self.position
    class Meta:
        ordering = ['id']


class Match(models.Model):
    match_id = models.CharField(max_length=20)
    home = models.CharField(max_length=20)
    score = models.CharField(max_length=20)
    away = models.CharField(max_length=20)
    week = models.ForeignKey('Week')
    def __str__(self):
        return self.match_id
    class Meta:
        ordering = ['id']
