from django.forms import ModelForm
from .models import Page
from django import forms


class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ["title", "body", "page_date", "picture"]

class LoginForm(forms.Form):
    name = forms.CharField(
        label='名前',
        max_length=10,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'ユーザー名を入力'
        })
    )
    password = forms.CharField(
        label='パスワード',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'パスワードを入力'
        })
    )
