from django import forms
from expenses.models import Post
from django.template.defaultfilters import slugify


class DateInput(forms.DateInput):
    input_type = 'date'


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'date', 'expense_amount', 'content']
        widgets = {
            'date': DateInput()
        }
