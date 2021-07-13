from django.urls import path
from django.views.generic.edit import DeleteView
from . import views

app_name = 'barmap'


urlpatterns = [
    path('', views.home, name='home'),
    path('barlist', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
]