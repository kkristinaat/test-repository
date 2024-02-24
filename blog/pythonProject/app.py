import blog
from blog import Blog
from post import Post
# a constant
MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create post, or "q" to quit.'
POST_TEMPLATE = '''
--- {} ---
{}
'''

blogs = dict()  # not {} - looks as set, set() # blog_name: Blog object

# show the user the available blogs
# let the user make a choice
# do smth with that choice
# eventually exit
def menu():
    print_blogs()
    selection = input(MENU_PROMPT)                                      # how to test it? -> check if the input method was called with the correct arg(string)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)

def print_blogs():
    for key, blog in blogs.items():                                     # iterate over the dict,key+value; it's the same as [(blog_name, Blog), (blog_name, Blog)] - list
        print('- {}'.format(blog))                                      # this doesn't do anything, it is MOCKING, with .assert we call fn - TRUE, now we can assume that print fn works without checking the console


# ask for blog title+name, store in blog dict.
def ask_create_blog():
    title = input('Enter your blog title: ')
    author = input('Enter your name ')

    blogs[title] = Blog(title, author)

def ask_read_blog() -> object:
    title = input('Enter the blog title you want to read: ')

    print_posts(blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
    blog_name = input('Enter the blog title you want to write a post in: ')
    title = input('Enter your post title: ')
    content = input('Enter your post content: ')

    blogs[blog_name].create_post(title, content)

if __name__ == '__main__':
        menu()