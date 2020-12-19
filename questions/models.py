''' Question Models '''

from django.db import models
from users.models import Profile


class SolveForm(models.Model):

    mentor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    points = models.IntegerField(default = 1)

    def __str__(self):
        return str(self.mentor.user.username)



class Question(models.Model):
    ''' Questions models '''
    TECHNOLOGY_CHOICES = [
        ('Data Science', 'Data Science'),
        ('Computer Science', 'Computer Science'),
        ('FrontEnd','FrontEnd'),
        ('BackEnd','BackEnd'),
        ('UI/UX','UI/UX'),
        ('English','English')
    ]

    TIME_CHOICES=[
        ('5 min','5 min'),
        ('15 min','15 min'),
        ('30 min','30 min'),
        ('45 min','45 min'),
        ('60 min','60 min'),
    ]

    author = models.ForeignKey("users.Profile", on_delete=models.CASCADE)
    description = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    time_to_solve = models.CharField(
        choices=TIME_CHOICES,
        max_length=60,
        null=True
    )
    technology_tag = models.CharField(
        choices=TECHNOLOGY_CHOICES,
        max_length=60,
        null=True
    )
    is_active = models.BooleanField(default=True)
    menthor = models.ForeignKey(SolveForm, on_delete=models.CASCADE, null=True)
    points = models.IntegerField(default = 1)

    def __str__(self):
        return str(self.description)


class Comment(models.Model):
    ''' Comments models'''

    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()


    def __str__(self):
        return str(self.post_date)


