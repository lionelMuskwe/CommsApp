from django.db import models

# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=50)
    # Question 1 For this quiz
    q1Question = models.CharField(max_length=100)
    q1Answer = models.CharField(max_length=100)
    # Question 2 For this quiz
    q2Question = models.CharField(max_length=100)
    q2Answer = models.CharField(max_length=100)


    def __str__ (self):
        return self.name