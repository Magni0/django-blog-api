from django.test import TestCase
from blog.models import Category, Post
from django.contrib.auth.models import User

class TestCreatePost(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        test_user = User.objects.create_user(username='testuser', password='pass')
        test_post = Post.objects.create(
            category_id=1, title='test title', excerpt='test excerpt', content='test content', author_id=1, slug='test-title', status='published'
        )
    
    def test_blog_content(self):
        post = Post.objects.get(id=1)
        cat = Category.objects.get(id=1)

        title = f'{post.title}'
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        content = f'{post.content}'
        status = f'{post.status}'

        self.assertEqual(title, 'test title')
        self.assertEqual(author, 'testuser')
        self.assertEqual(excerpt, 'test excerpt')
        self.assertEqual(content, 'test content')
        self.assertEqual(status, 'published')

        self.assertEqual(str(post), 'test title')
        self.assertEqual(str(cat), 'django')