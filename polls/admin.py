from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    modle = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline,]

admin.site.register(Question)
