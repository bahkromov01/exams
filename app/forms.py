from django import forms
from app.models import Product, Comment, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'product': forms.HiddenInput()
        }
