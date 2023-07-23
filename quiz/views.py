from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from quiz.models import Question, Option


class HomeView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'home.html', {})


class QuizListView(LoginRequiredMixin, View):
    redirect_unauthenticated_users = True

    def get(self, request, *args, **kwargs):
        return render(request, 'quiz-list.html', {})


class AddQuestionOptions(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return render(request, 'add-question.html', {})

    def post(self, request, *args, **kwargs):
        form = request.POST
        question_text = form.getlist('question_text')
        options = form.getlist('option[]')

        question_obj = Question.objects.create(question_text=question_text)

        for opt in range(len(options)):
            Option.objects.create(question=question_obj, option_text=options[opt],
                                  is_correct=True if form.get(f"correct{opt}") else False)

        return render(request, 'add-question.html', {})
