from . import views
from django.urls import path

urlpatterns = [
    path("", views.news_page),
    path("create", views.create),
    path("<int:pk>", views.NewsDetailView.as_view(), name="news_detail"),
    path("<int:pk>/update", views.NewsUpdateView.as_view(), name="news_update"),
    path("<int:pk>/delete", views.NewsDeleteView.as_view(), name="news_delete"),
]
