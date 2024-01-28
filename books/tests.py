from django.test import TestCase
from django.urls import reverse

from .models import Books

# Create your tests here.

class BookListTest(TestCase):
    def test_book_list(self):
        Books.objects.create(title='title1',price=12400,description='description1',isbn=123456)
        Books.objects.create(title='title2',price=12300,description='description2',isbn=123452)
        Books.objects.create(title='title3',price=44400,description='description3',isbn=123453)

        books=Books.objects.all()
        book_list=self.client.get(reverse('books:book-list'))
        for book in books:
            self.assertContains(book_list,book.title)

    def test_detail(self):
        book=Books.objects.create(title='title2',price=12300,description='description2',isbn=123452)
        book_detail=self.client.get(reverse('books:book-detail',kwargs={'pk':book.pk}))
        self.assertContains(book_detail, book.title)