from django.forms import ModelForm
from .models import FormModel

class FormForm(ModelForm):
    class Meta:
        model = FormModel
        # fields = ['name', 'favorite_color', 'cats_or_dogs']
        fields = '__all__'
