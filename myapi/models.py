# models.py
from django.db import models


class Exercise(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    Sets = models.IntegerField()
    Reps = models.CharField(max_length=5)
    RestTime = models.IntegerField()
    ManagedReps = models.IntegerField()
    ManagesSets = models.IntegerField()
    CompletedDate = models.CharField(max_length=20)
    IsCompleted = models.BooleanField()

    def str(self):
        return self.Title


class ExerciseList(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    Exercises = models.ManyToManyField(Exercise)

    def str(self):
        return self.Title