from django.urls import path
from .views import *

urlpatterns = [
    path('', shoplist),
    path('shopsingle/', shopsingle)
]