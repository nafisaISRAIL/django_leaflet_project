from django import forms
from master.scraping.models import Article


class UpdateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"


class DeleteAtricleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = []
