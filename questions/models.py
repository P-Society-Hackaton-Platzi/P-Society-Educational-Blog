''' Question Models '''

from django.db import models
from users.models import Profile


class Technologie(models.Model):
    ''' Tecnologies tag models '''
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class SolveForm(models.Model):

    mentor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    points = models.IntegerField(default = 1)

    def __str__(self):
        return str(self.mentor.user.username)



class Question(models.Model):
    ''' Questions models '''
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    time_to_solve = models.DurationField()
    technology_tag = models.ForeignKey(Technologie, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    menthor = models.ForeignKey(SolveForm, on_delete=models.CASCADE)
    points = models.IntegerField(default = 1)

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    ''' Comments models'''

    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()


    def __str__(self):
        return str(self.post_date)


