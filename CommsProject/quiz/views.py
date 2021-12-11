from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

# Importing models
from .models import Quiz

# Create your views here.
class ShowAvailableTrainingsView(ListView):
    template_name = "AvailableQuizzes.html"
    model = Quiz
    querySet = Quiz.objects.all()
    context_object_name = "quizzes"

    # def get_queryset(self, *args, **kwags):
    #     qs = super().get_queryset(*args, **kwags)
    #     return qs

class ShowQuizDetailView(DetailView):
    model = Quiz
    template_name = "TrainingPage.html"
    context_object_name = "quiz"

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(*args, **kwargs)
    
    print("This bit of code ran")
    
