from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article  # add input fields to be displayed in template
        fields = [
            "title",
            "image",
            "content",
        ]


