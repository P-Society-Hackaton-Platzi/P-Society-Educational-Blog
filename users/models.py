''' Users Models '''

from django.db import models
from django.contrib.auth.models import User

''' cloudinary models '''
from cloudinary.models import CloudinaryField


class Profile(models.model):
    ''' Profile model extends from User base model '''

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = CloudinaryField('image')
    menthor_points = models.IntegerField()
    calendar = models.URLField(max_length=255)
    availability = models.BooleanField(defautl=True)


    def __str__(self):
        return str(self.user.username)