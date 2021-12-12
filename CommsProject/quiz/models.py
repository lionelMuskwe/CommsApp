from django.db import models

# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=50)
    # Question 1 For this quiz
    q1Question = models.CharField(max_length=100)
    q1Answer = models.CharField(max_length=100)
    q1Explanation = models.CharField(max_length=10000, null=True, blank=True)
    # Question 2 For this quiz
    q2Question = models.CharField(max_length=100)
    q2Answer = models.CharField(max_length=100)
    q2Explanation = models.CharField(max_length=10000, null=True, blank=True)
     # Question 3 For this quiz
    q3Question = models.CharField(max_length=100, null=True, blank=True)
    q3Answer = models.CharField(max_length=100, null=True, blank=True)
    q3Explanation = models.CharField(max_length=10000, null=True, blank=True)


    def __str__ (self):
        return self.name