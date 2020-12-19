''' Questions Forms '''
from django import forms
from questions.models import Question

TECHNOLOGY_CHOICES = [
    ('Data Science', 'Data Science'),
    ('Computer Science', 'Computer Science'),
    ('FrontEnd','FrontEnd'),
    ('BackEnd','BackEnd'),
    ('UI/UX','UI/UX'),
    ('English','English')
]

class QuestionForm(forms.Form):
    ''' Question model form '''

    time_to_solve = forms.DurationField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '¿Cuanto tiempo crees necesitar para solucionar tu duda?',
                'class': 'form-control',
                'required': True
                }
        )
    )

    description = forms.CharField(min_length=4,
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Haz tu pregunta',
                'class': 'form-control',
                'required': True
                }
        )
    )

    technology = forms.ChoiceField(
        widget=forms.Select(
            attrs = {
                'class':'form-control'    
            }),
        choices=TECHNOLOGY_CHOICES,
        required = True,
    )
