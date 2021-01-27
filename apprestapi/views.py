from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.response import Response

from .models import Article, Author
from .serializers import ArticleSerializer, AuthorSerializer


class ArticleView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author'))
        return serializer.save(author=author)


class SingleArticleView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class AuthorView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.validated_data)

        if Author.objects.filter(email=request.data.get('email')).count() > 0:
            content = {'error': f'This email already exists.'}
            return Response(content, status=status.HTTP_409_CONFLICT, headers=headers)
        self.perform_create(serializer, request)
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, request):
        if Author.objects.filter(email=request.data.get('email')).count() > 0:
            return False
        else:
            serializer.save()


class SingleAuthorView(RetrieveUpdateDestroyAPIView, UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def put(self, request, *args, **kwargs):
        author_id = kwargs
        try:
            author = Author.objects.get(email=request.data['email'])
            if author.id != author_id['pk']:
                content = {'error': f'User with {request.data["email"]} email already exists'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
            else:
                return self.partial_update(request, *args, **kwargs)
        except Author.DoesNotExist:
            return self.partial_update(request, *args, **kwargs)
