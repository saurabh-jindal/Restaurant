from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('contact/', views.contact, name='contact'),
    path('booktable/', views.booktable, name='booktable'),

]