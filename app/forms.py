from django import forms
from app.models import Comment, Order


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'email')


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

