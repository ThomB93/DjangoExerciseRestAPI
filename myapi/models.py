# models.py
from django.db import models


class Exercise(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    Sets = models.IntegerField()
    Reps = models.CharField(max_length=5)
    RestTime = models.IntegerField()
    ManagedReps = models.IntegerField(blank=True)
    ManagedSets = models.IntegerField(blank=True)
    CompletedDate = models.CharField(max_length=20, blank=True)
    IsCompleted = models.BooleanField(blank=True)

    def str(self):
        return self.Title


class ExerciseList(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    Exercises = models.ManyToManyField(Exercise)

    def str(self):
        return self.Title
