from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Article, Author
from .serializers import ArticleSerializer, AuthorSerializer

# Create your views here.


class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})

    def post(self, request):
        article = request.data.get('article')
        # Create an article from the above data
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Article '{}' created successfully".format(article_saved.title)
        })


class ArticleViewChange(APIView):
    def put(self, request, pk):
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            try:
                article_saved = serializer.save()
            except:
                article_saved = get_object_or_404(Author.objects.all(), data['author_id'])
        return Response({
            "success": "Article '{}' updated successfully".format(article_saved.title)
        })

    def delete(self, request, pk):
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Article with id `{}` has been deleted.".format(pk)
        }, status=204)


class AuthorView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response({"authors": serializer.data})

    def post(self, request):
        author = request.data.get('author')
        # Create an article from the above data
        serializer = AuthorSerializer(data=author)
        if serializer.is_valid(raise_exception=True):
            # author_email = Author.objects.get(email=serializer.email)
            try:
                Author.objects.get(email=author['email'])
                return Response({
                    "error": "Such email already exists"
                })
            except Author.DoesNotExist:
                author_saved = serializer.save()
                return Response({
                    "success": "Author '{}' created successfully".format(author_saved.name)
                })
