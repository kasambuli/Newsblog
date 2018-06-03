from django.forms import Form
from django import forms
from .models import Profile,User,Comments,News

class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar','bio','email']
        exclude = ['user']

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
        exclude = ['user']

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['image','title','news']
        exclude = ['user']