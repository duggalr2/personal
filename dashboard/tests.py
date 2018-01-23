from django.test import TestCase
from .models import Book
from .forms import BookForm


# models test
class BookTest(TestCase):

    def create_book(self, title="only a test"):
        return Book.objects.create(book_name=title)

    def test_book_creation(self):
        w = self.create_book()
        self.assertTrue(isinstance(w, Book))
        self.assertEqual(w.book_name, 'only a test')

    def test_valid_form(self):
        w = Book.objects.create(book_name='Foo')
        data = {'book_name': w.book_name}
        form = BookForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        w = Book.objects.create(book_name='')
        data = {'book_name': w.book_name}
        form = BookForm(data=data)
        self.assertFalse(form.is_valid())
