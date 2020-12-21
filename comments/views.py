from django.shortcuts import render
from .forms import UserCommentForm
from .models import UserComment


def create_comment(request):
    user_comments = UserComment.objects.all()
    form = UserCommentForm()
    data = {
        "form": form,
        "user_comments": user_comments,
    }
    return render(request, "news/details_view.html", data)
