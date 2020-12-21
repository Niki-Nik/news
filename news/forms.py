from .models import News
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ["title", "anons", "full_text"]
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название новости"
            }),
            "anons": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Анонс новости"
            }),
            "date_time": DateTimeInput(attrs={
                "class": "form-control",
                "placeholder": "Дата публикации"
            }),
            "full_text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Текст новости"
            }),
        }
