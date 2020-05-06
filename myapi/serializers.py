# serializers.py
from rest_framework import serializers
from .models import Exercise, ExerciseList

class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exercise
        fields = ('Id', 'Title', 'Sets', 'Reps', 'RestTime', 'ManagedReps','ManagedSets','CompletedDate','IsCompleted')
		
class ExerciseListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExerciseList
        fields = ('Id', 'Title', 'Exercises')
