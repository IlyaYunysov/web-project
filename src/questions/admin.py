from django.contrib import admin
from .models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = 'title', 'created'


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = 'text', 'question', 'created'