from django.test import TestCase
from apprestapi.models import Article, Author


class AuthorModelTest(TestCase):

    def SetUpData(self):
        Author.objects.create(
            id=2,
            name='Test Model 2',
            email='olgalyalyueva+testmodel_2@gmail.com'
        )
    a = Author.objects.get(id=2)

    def test_name_max_length(self):
        max_length = self.a._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)


class ArticleModelTest(TestCase):

    def SetUpData(self):
        author = Author.objects.create(
            id=3,
            name='Test Model 3',
            email='olgalyalyueva+testmodel_3@gmail.com'
        )

        Article.objects.create(
            id=2,
            title='Test Model Title',
            description='Test Model Description',
            body='Test Model Body',
            author=author
        )

    article = Article.objects.get(id=2)

    def test_title_max_length(self):
        max_length = self.article._meta.get_field('title').max_length
        self.assertEquals(max_length, 120)

    def test_description_max_length(self):
        max_length = self.article._meta.get_field('description').max_length
        self.assertEquals(max_length, 3000)

    def test_body_max_length(self):
        max_length = self.article._meta.get_field('body').max_length
        self.assertEquals(max_length, 5000)
