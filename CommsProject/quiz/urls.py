from django.urls import path

from .views import ShowAvailableTrainingsView, ShowQuizDetailView, HomePageView


urlpatterns = [
    path("trainings/",ShowAvailableTrainingsView.as_view(), name="quizzes-all-quizzes"),
    path("", HomePageView.as_view(), name="home-page"),
    path("<int:pk>/", ShowQuizDetailView.as_view(), name="quiz-detail")
]

