from django.urls import path
from .views import (
    AuthorListCreateAPIView,
    AuthorDetailAPIView,
    BookListCreateAPIView,
    BookDetailAPIView,
)

urlpatterns = [
    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetailAPIView.as_view(), name='author-detail'),

    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
]