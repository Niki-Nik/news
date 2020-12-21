from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_page(request):
    news = News.objects.order_by("-date_time")
    return render(request, "news/news_page.html", {"news": news})


class NewsDetailView(DetailView):
    model = News
    template_name = "news/details_view.html"
    context_object_name = "post"


class NewsUpdateView(UpdateView):
    model = News
    template_name = "news/create.html"
    # fields = ["title", "anons", "full_text"]
    form_class = NewsForm


class NewsDeleteView(DeleteView):
    model = News
    success_url = '/news/'
    template_name = "news/news_delete.html"


def create(request):
    error = ""
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/news")
        else:
            error = "Форма была неверной!"
    form = NewsForm()
    data = {
        "form": form,
        "error": error,
    }
    return render(request, "news/create.html", data)
