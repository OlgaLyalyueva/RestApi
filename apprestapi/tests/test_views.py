from django.test import TestCase
from apprestapi.models import Author, Article
from apprestapi.serializers import AuthorSerializer, ArticleSerializer


class AutorAndArticleViewTest(TestCase):
    author = Author.objects.all()
    article = Article.objects.all()

    def setUp(self):
        author = Author.objects.create(
            id=1,
            name='Test Fox',
            email='olgalyalyueva+test_fox@gmail.com'
        )

        Article.objects.create(
            id=1,
            title='Test Title',
            description='Test Description',
            body='Test Body',
            author=author
        )

    def test_view_authors_url_accessible(self):
        response = self.client.get('/api/authors/')
        serializer = AuthorSerializer(self.author, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_view_author_has_contants(self):
        response = self.client.get('/api/authors/1')
        author = Author.objects.get(id=1)
        self.assertContains(response, author.id)
        self.assertContains(response, author.name)
        self.assertContains(response, author.email)

    def test_view_articles_url_accessible(self):
        response = self.client.get('/api/articles/')
        serializer = ArticleSerializer(self.article, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_view_articles_has_contants(self):
        response = self.client.get('/api/articles/1')
        article = Article.objects.get(id=1)
        self.assertContains(response, article.id)
        self.assertContains(response, article.description)
        self.assertContains(response, article.body)
        self.assertContains(response, article.author.id)
