from .models import UserComment
from django.forms import ModelForm, TextInput, Textarea


class UserCommentForm(ModelForm):
    class Meta:
        model = UserComment
        fields = ["user_name", "comment_text"]
        widgets = {
            "user_name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название новости"
            }),
            "comment_text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Анонс новости"
            }),
        }
