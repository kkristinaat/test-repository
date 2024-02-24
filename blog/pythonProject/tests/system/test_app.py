# will test through entire system
from unittest import TestCase            # unittest - module, TC - class, patch - fn
from unittest.mock import patch          # (will patch the print fn)
# from app import * -> app.menu()
import app                              # -> menu() -- more readible
from blog import Blog
from post import Post


class AppTest(TestCase):
    def setUp(self):    # will run before each test
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}

    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_print:  # want to patch print with module "builtins"
            app.menu()

            mocked_print.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch ('app.ask_create_blog') as mocked_ask_create_blog:
                app.menu()

                mocked_ask_create_blog.assert_called()

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'Test Two', 'Test Author Two', 'q')
            app.menu()

            self.assertIsNotNone(app.blogs['Test Two'])

    def test_menu_calls_print_blogs(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.print_blogs') as mocked_print_blogs:
                mocked_input.side_effect = ('l', 'q')
                app.menu()

                mocked_print_blogs.assert_called()

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input',
                       return_value='q'):
                app.menu()

                mocked_print_blogs.assert_called()

    def test_menu_calls_ask_read_blogs(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_read_blog') as mocked_ask_read_blog:
                mocked_input.side_effect = ('r', 'Test', 'q')
                app.menu()

                mocked_ask_read_blog.assert_called()

    def test_menu_calls_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_post') as mocked_ask_create_post:
                mocked_input.side_effect = ('p', 'Test', 'New Post', 'New Content', 'q')
                app.menu()

                mocked_ask_create_post.assert_called()


    def test_print(self):
       # with patch('unittest.mock.patch') as mocked_print: #want to receive the module that this fn is in, to patch patch
        with patch('builtins.print') as mocked_print:               # want to patch print with module "builtins"
                app.print_blogs()
                mocked_print.assert_called_with('- Test by Test Author (0 posts)') #

    # We've patched the print fn as mocked print; we call the print block, which call print as long as there are blogs to print.
    # We assert that it has been called with this value here.
    # As soon as we patch, we replace this print fn by our mocked print fn and then with unittest this allows us to check whether it was called or not.
    # Naturally this test is going to fail because we don't have a blog right now, so this is not going to
    # print anything. But we can make a blog - import blog.

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author') # returns our 2 inputs
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))   # make sure that the blog was created

    def test_ask_read_blog(self):
        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()   # now we can check if the fn was called or if the print fn was called

            mocked_print_posts.assert_called_with(app.blogs['Test'])

    def test_print_posts(self):
        blog = app.blogs['Test']
        blog.create_post('Test Post', 'Test Content')
        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)

            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post('Post title', 'Post content')
        expected_print = '''
--- Post title ---
Post content
'''
        with patch('builtins.print') as mocked_print:
            app.print_post(post)

            mocked_print.assert_called_with(expected_print)

    def test_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Title', 'Test Content')

            app.ask_create_post()

            self.assertEqual(app.blogs['Test'].posts[0].title, 'Test Title')
            self.assertEqual(app.blogs['Test'].posts[0].content, 'Test Content')

