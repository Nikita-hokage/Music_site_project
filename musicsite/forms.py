from django import forms

from .models import Janr, Song, Author




class AddJanrF(forms.ModelForm):
    class Meta:
        model = Janr
        fields = '__all__'

class AddSongF(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'

class AddAuthorF(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'