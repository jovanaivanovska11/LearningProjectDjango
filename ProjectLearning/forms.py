from django import forms
from .models import Person, Lecture, Forum, Reply

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = '__all__'

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = '__all__'