from django import forms

class ProfileForm(forms.Form):

    picture = forms.ImageField()
    calendar = forms.URLField(max_length=255, required=True)
    availability = models.BooleanField(default=True)