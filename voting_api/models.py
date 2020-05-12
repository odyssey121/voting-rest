from django.db import models
from django.contrib.auth.models import User


# ОПРОС
class Voting(models.Model):
    name = models.CharField(max_length=100, unique=True)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(null=True)
    desc = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ("-start_date",)

    def __str__(self):
        return f"{self.name}"


# ВОПРОС
class Question(models.Model):
    voting = models.ForeignKey(Voting, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=100, blank=False, null=False)
    question_type = models.CharField(choices=[('text', 'text'), ('single', 'single'), ('multiple', 'multiple')],
                                     max_length=10, blank=False, null=False)

    class Meta:
        unique_together = ("voting", "question_text")

    def __str__(self):
        return f"voting ={self.voting} || question_text = {self.question_text}"


# ОТВЕТ
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text

    class Meta:
        unique_together = ("question", "user")
