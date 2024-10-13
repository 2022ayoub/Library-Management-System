from django import forms
from .models import Book,Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=[
            'name'
        ]
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'})
        }




class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        # fields='__all__'
        fields=[
            'title',
            'author',
            'bookImg',
            'authorImg',
            'pages',
            'price',
            'rental_price_day',
            'rental_period',
            'status',
            'category',
        ]
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'bookImg':forms.FileInput(attrs={'class':'form-control'}),
            'authorImg':forms.FileInput(attrs={'class':'form-control'}),
            'pages':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'rental_price_day':forms.NumberInput(attrs={'class':'form-control'}),
            'rental_period':forms.NumberInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
        }

