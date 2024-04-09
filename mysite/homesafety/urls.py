from django.urls import path
from homesafety import views
from .views import get_csrf_token_view

urlpatterns=[
    path('',views.data,name='data'),
     path('csrf_token/', get_csrf_token_view, name='get_csrf_token'),
]