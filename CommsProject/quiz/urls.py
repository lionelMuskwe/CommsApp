from django.urls import path

from .views import ShowAvailableTrainingsView, ShowQuizDetailView


urlpatterns = [
    path("",ShowAvailableTrainingsView.as_view(), name="quizzes-all-quizzes"),
    path("<int:pk>/", ShowQuizDetailView.as_view(), name="quiz-detail")
]

