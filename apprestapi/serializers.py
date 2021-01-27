from rest_framework import serializers
from .models import Article, Author


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'description', 'body', 'author')
        read_only_fields = ('id',)

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'email')
        read_only_fields = ('id',)
