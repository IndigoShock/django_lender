from django.test import TestCase, RequestFactory
from .models import Book


# Create your tests here.
class TestBookModel(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title='Feed the cat', description='She is hangry')
        Book.objects.create(title='blarp', description='wat stick')
        Book.objects.create(title='Gnarf', description='wat dis')

    def test_book_titles(self):
        self.assertEqual(self.book.title == 'Feed the cat')

    def test_book_detail(self):
        book = Book.objects.get(title='Gnarf')

        self.assertEqual(book.description, 'wat dis')


class TestBookViews(TestCase):
    def setUp(self):
        self.request = RequestFactory()
        self.book_one = Book.objects.create(title='blarp', description='wat stick')
        self.book_two = Book.objects.create(title='Gnarf', description='wat dis')

    def test_book_detail_view(self):
        from .views import book_detail_view
        request = self.request.get('')
        response = book_detail_view(request, f'{self.book_one.id}')
        self.assertIn(b'wat dis', response.content)

    def test_book_detail_status(self):
        from .views import book_detail_view
        request = self.request.get('')
        response = book_detail_view(request, f'{self.book_one.id}')
        self.assertIn(200, response.status_code)
