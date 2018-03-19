from django.test import TestCase
from core.models import User
from feed.models import Event
from ucc.models import Post
from like.models import Like


class TestEvent(TestCase):

    def setUp(self):
        self.User1 = User.objects.create(username='User1', password='dsghfjhdsgfjadsgfjdasgfjdas')
        self.User2 = User.objects.create(username='User2', password='sghdfhsgdfjagjdgfsahgfajsgf')

    def testLikesAchieveEvent(self):
        self.userPost = Post.objects.create(author=self.User1, content='aadsjhfadsjfhas')
        Like.objects.create(content_object=self.userPost, author=self.User1)
        self.assertEqual(Event.objects.all().count(), 1)
        Like.objects.create(content_object=self.userPost, author=self.User2)
        self.assertEqual(Event.objects.all().count(), 2)
        Like.objects.first().delete()
        self.assertEqual(Event.objects.all().count(), 1)

    def tearDown(self):
        self.User1.delete()
        self.User2.delete()