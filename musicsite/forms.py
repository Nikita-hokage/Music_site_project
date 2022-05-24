from django import forms

from musicsite.models import Janr, Song

from musicsite.models import Author


class AddJanrF(forms.Form):
    class Meta:
        model = Janr
        fields = '__all__'

class AddSongF(forms.Form):
    class Meta:
        model = Song
        fields = '__all__'

class AddAuthorF(forms.Form):
    class Meta:
        model = Author
        fields = '__all__'