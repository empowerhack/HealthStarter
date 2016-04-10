from django.contrib import admin

from .models import Question, Choice, Tip

class QuestionAdmin(admin.ModelAdmin):
    fields = ('question_text')

class TipAdmin(admin.ModelAdmin):
    fields = ('tip')

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Tip)


