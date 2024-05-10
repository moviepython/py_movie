from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['movie', 'review_text', 'rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['movie'].widget.attrs.update({'class': 'form-control'})
        self.fields['review_text'].widget.attrs.update({'class': 'form-control', 'rows': 5})
        self.fields['rating'].widget.attrs.update({'class': 'form-control'})
