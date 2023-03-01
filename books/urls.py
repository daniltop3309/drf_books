from django.contrib import admin
from django.urls import path
from book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', views.api_overview, name='api_overview'),
    path('api/v1/get_books/', views.get_books, name='get_books'),
    path('api/v1/get_book/<int:pk>/', views.get_book, name='get_book'),
    path('api/v1/create_book/', views.create_book, name='create_book'),
    path('api/v1/update_book/<int:pk>/', views.update_book, name='update_book'),
    path('api/v1/delete_book/<int:pk>/', views.delete_book, name='delete_book'),
]
