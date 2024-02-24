from unittest import TestCase
from post import Post

class PostTest(TestCase): #each testsuite is a class, has to inherit from a particular TC
    def test_create_post(self): #starts with - test_;
        p = Post("Test", "Test Content")

        self.assertEqual("Test", p.title)
        self.assertEqual("Test Content", p.content) #when I change the _init methos = test will fail

    def test_json(self):
        p = Post("Test", "Test Content")
        expected = {'title': 'Test', 'content': 'Test Content'}  #make sure p.json == expected

        self.assertDictEqual(expected, p.json()) # check the key and values are the same


