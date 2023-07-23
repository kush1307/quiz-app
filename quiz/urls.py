from django.urls import path

from quiz.views import HomeView, QuizListView, AddQuestionOptions

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('quiz/', QuizListView.as_view(), name='quiz-list'),
    path('add-question/', AddQuestionOptions.as_view(), name="add-question")
]
