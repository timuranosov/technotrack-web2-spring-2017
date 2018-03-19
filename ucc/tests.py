from django.test import TestCase

from core.models import User
from feed.models import Event
from ucc.models import Post


class TestEvent(TestCase):
    def setUp(self):
        self.User1 = User.objects.create(username='User1', password='dsghfjhdsgfjadsgfjdasgfjdas')
        self.User2 = User.objects.create(username='User2', password='sghdfhsgdfjagjdgfsahgfajsgf')

    def testPostCreate(self):
        self.userPost = Post.objects.create(author=self.User1, content='aadsjhfadsjfhas')
        self.assertEqual(self.userPost.event.exists(), True)
        self.userPost.delete()
        self.assertEqual(Event.objects.all().count(), 0)

    def tearDown(self):
        self.User1.delete()
        self.User2.delete()
