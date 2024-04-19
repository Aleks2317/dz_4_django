from django import forms
from .models import Product
import datetime


class Product_update_Form(forms.Form):
    image = forms.ImageField()
    name = forms.ChoiceField(choices=[(a.id, a.name) for a in Product.objects.all()])
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))
    price = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    quantity = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    date_registration = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
    }))



# class Post_Form(forms.Form):
#     title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Название статьи',
#     }))
#     content = forms.CharField(widget=forms.Textarea(attrs={
#         'class': 'form-control'}))
#     data_publication = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={
#         'class': 'form-control',
#         'type': 'date',
#     }))
#     author = forms.ChoiceField(choices=[(a.id, a.name) for a in Author.objects.all()])
#     category = forms.ChoiceField(choices=[
#         ('sports', 'Спорт'),
#         ('cooking', 'Рецепты'),
#         ('art', 'Искусство'),
#         ('fantasy', 'Фэнтези'),
#         ('documentation', 'Документация'),
#         ('humor', 'Юмор')
#         ])
#     flag_publicaton = forms.BooleanField(label='Опубликовать', required=False, widget=forms.CheckboxInput(attrs={
#         'class': 'form-check-input'}))