from django.contrib import admin

from quiz.models import QuizAttempt, Question, Option, QuizResult

# Register your models here.

admin.site.register(QuizAttempt)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(QuizResult)
