from django.test import TestCase
from django.urls import reverse

from .models import Book

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title='a book',
            author='an author',
            price='99.99'
        )
    
    def test_book_listing(self):
        self.assertEqual(f"{self.book.title}",'a book')
        self.assertEqual(f"{self.book.author}",'an author')
        self.assertEqual(f"{self.book.price}",'99.99')
    
    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'a book')
        self.assertTemplateUsed(response,'books/book_list.html')
    
    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12345')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'a book')
        self.assertTemplateUsed(response,'books/book_detail.html')