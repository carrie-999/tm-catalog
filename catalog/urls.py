from django.urls import path
from .views import NameListView, NameCreateView, test_view

app_name = 'catalog'
urlpatterns = [
    path('test/', test_view, name='test'),         # ← nasz test
    path('', NameListView.as_view(), name='list'),
    path('register/', NameCreateView.as_view(), name='register'),
]
