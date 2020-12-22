from django.urls import path
from .views import ArticleView, ArticleViewChange, AuthorView


app_name = "apprestapi"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('apprestapi/', ArticleView.as_view()),
    path('apprestapi/<int:pk>', ArticleViewChange.as_view()),
    path('authors/', AuthorView.as_view()),
]
