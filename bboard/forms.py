from django.forms import ModelForm
from .models import Bb

class BbForm(Model.form):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')