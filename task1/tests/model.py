from pprint import pprint

from django.test import TestCase
from model_bakery import baker
from task1.models import Post, User


class TestTask1Model(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        testuser = User.objects.create(username="testuser", password="12345")
        testuser2 = User.objects.create(username="testuser2", password="12345")
        cls.new = Post.objects.create(
            title="django", content="nove conteudo", slug="django"
        )
        cls.new.likes.set([testuser.pk, testuser2.pk])

    def test_model_str(self):
        self.assertEqual(str(self.new), "django")

    def test_post_has_an_author(self):
        self.assertEqual(self.new.likes.count(), 2)

    def test_get_absolute_url(self):
        self.new.slug = Post.objects.get(id=1)

        self.assertEqual("/single/django", self.new.slug.get_absolute_url())


class TestNew(TestCase):
    def setUp(self) -> None:
        self.post = baker.make("task1.Post")
        pprint(self.post.__dict__)

    def test_model_str(self):
        title = Post.objects.create(title="Django testing")
        content = Post.objects.create(content="this is some content")
        self.assertEqual(str(title), "Django testing")
