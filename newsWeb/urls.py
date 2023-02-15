from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', articles, name='articles'),
    path('create/', news_create, name='news_create'),
    path('update/<int:pk>/', news_update, name='news_update'),
    path('delete/<int:pk>/', news_delete, name='news_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
