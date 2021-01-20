from django.urls import path
from .views import ArticleView, SingleArticleView, AuthorView, SingleAuthorView


app_name = "apprestapi"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>', SingleArticleView.as_view()),
    path('authors/', AuthorView.as_view()),
    path('authors/<int:pk>', SingleAuthorView.as_view()),
]
