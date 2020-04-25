# views.py
from rest_framework import viewsets
from .serializers import ExerciseSerializer, ExerciseListSerializer
from .models import Exercise, ExerciseList


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all().order_by('Title')
    serializer_class = ExerciseSerializer
	
class ExerciseListViewSet(viewsets.ModelViewSet):
    queryset = ExerciseList.objects.all().order_by('Title')
    serializer_class = ExerciseListSerializer