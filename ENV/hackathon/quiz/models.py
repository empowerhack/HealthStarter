from __future__ import unicode_literals

from django.db import models

from django.forms import ModelForm


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    correct_choice = models.BooleanField(default=0)

    def __str__(self):
        return self.choice_text


class Tip(models.Model):
    tip = models.CharField(max_length=200)

    def __str__(self):
        return self.tip
