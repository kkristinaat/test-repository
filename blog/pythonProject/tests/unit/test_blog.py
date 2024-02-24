from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')
        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)  # can use also self.assertEqual(0, len(b.posts))

    def test_repr(self):
        b = Blog('Test', 'Test Author')  # blogobject
        b2 = Blog('My day', 'Rolf')
        self.assertEqual(b.__repr__(),
                         'Test by Test Author (0 posts)')  # what we will see instead of generic python description
        # test will fail, but we can make it pass - by changing blog.py ( change "pass")
        self.assertEqual(b2.__repr__(), 'My day by Rolf (0 posts)')

    def test_repr_multiple_posts(self):  # testing multiple values, boundaries
        b = Blog('Test', 'Test Author')
        b.posts = ['test']
        b2 = Blog('My day', 'Rolf')
        b2.posts = ['test', 'another']
        self.assertEqual(b.__repr__(), 'Test by Test Author (1 post)')
        self.assertEqual(b2.__repr__(), 'My day by Rolf (2 posts)')


