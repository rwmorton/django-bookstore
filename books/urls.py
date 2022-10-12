from django.urls import path

from books.models import Book

from .views import BookListView, BookDetailView

urlpatterns = [
    path('',BookListView.as_view(),name='book_list'),
    path('<uuid:pk>',BookDetailView.as_view(),name='book_detail'),
]
