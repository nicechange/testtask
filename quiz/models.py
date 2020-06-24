from django.db import models
from django.conf import settings

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=4096)
    description = models.CharField(max_length=4096)
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
           return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=4096)
    TYPE_CHOISES = (
        ('text', 'Text'),
        ('one_choice', 'One choice'),
        ('many_choices', 'Many choices'),
    )
    type = models.CharField(null=True, max_length=409, choices=TYPE_CHOISES,
                            default='Text', verbose_name="Тип ответа")

    def __str__(self):
           return self.title

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=4096)
    lock_other = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Answer(models.Model):
    user_code = models.CharField(max_length=40)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choices = models.ManyToManyField(Choice, default=None, blank=True)
    answr = models.CharField(max_length=4096, default='', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answr