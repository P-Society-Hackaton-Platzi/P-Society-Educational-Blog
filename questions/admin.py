from django.contrib import admin

# Register your models here.
from questions.models import Technologie, Question, Comment, SolveForm

admin.site.register(Technologie)
admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(SolveForm)