from django.contrib import admin

# Register your models here.
from questions.models import Question, Comment, SolveForm

admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(SolveForm)