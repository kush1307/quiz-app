from django.contrib.auth.models import User
from django.db import models


class QuizAttempt(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} -- {self.user.username}"


class Question(models.Model):

    question_text = models.TextField()

    def __str__(self):
        return f"{self.question_text}"


class Option(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question_id} -- {self.option_text} -- {self.is_correct}"


class QuizResult(models.Model):

    quiz_attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.quiz_attempt_id}"
