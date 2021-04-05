from .models import Posts

from django import forms


class CreatePost(forms.ModelForm):
    class Meta:
        model = Posts
        fields = '__all__'
