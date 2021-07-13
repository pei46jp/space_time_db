from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import generic
from .models import Category, Bar



def home(request):
    return render(request, 'barmap/home.html')



class IndexView(generic.ListView):
    model = Bar


class DetailView(generic.DetailView):
    model = Bar


class CreateView(generic.edit.CreateView):
    model = Bar
    fields = '__all__'


class UpdateView(generic.edit.UpdateView):
    model = Bar
    fields = '__all__'


class DeleteView(generic.edit.DeleteView):
    model = Bar
    success_url = reverse_lazy('barmap:index')