from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    # path('<int:id>',views.book_detail, name = 'bd'),
    path('<slug:slug>',views.book_detail, name = 'bd'),
]