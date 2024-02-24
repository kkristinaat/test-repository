from post import Post

class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return '{} by {} ({} post{})'.format(self.title, self.author, len(self.posts),
                                             's' if len(self.posts) != 1 else '')
                                                                          # wrapper method; what we see repr the blog when we are for ex. debugging
                                                                          # return 'Test by Test Author (0 posts)' - test will pass; not good - for a lot of tests TDD!!! - write a test, which fails.
                                                                          # to make 2 tests pass: return '{} by {} (0 posts)'.format(self.title, self.author)
    def create_post(self, title, content):                                # will not receive post_object, have to create it
        self.posts.append(Post(title,content))


    def json(self):
            return {
                "title": self.title,
                "author": self.author,
                "posts": [post.json() for post in self.posts]              # integration method
            }

