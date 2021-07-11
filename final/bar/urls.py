from collections import namedtuple
from django.urls import path
from . import views

app_name = 'bar'

urlpatterns = [
    path('', views.base, name='base'),
    path('overview/', views.overview, name='overview'),
    path('overview/<int:id>', views.detail, name='detail'),
    path('new', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:id>/edit', views.edit, name='edit'),
    path('<int:id>/update', views.update, name='update'),
    path('<int:id>/delete', views.delete, name='delete'),
]