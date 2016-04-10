from django.contrib import admin

from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    fields = ('question_text')

admin.site.register(Question)
admin.site.register(Choice)


