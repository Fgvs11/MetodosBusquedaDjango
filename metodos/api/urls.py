from django.urls import path, include
from .views import NodoView

urlpatterns=[
    path('nodo',NodoView.as_view(), name='nodo')
]