from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import generic
from .models import Category, Bar
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied



def home(request):
    return render(request, 'barmap/home.html')



class IndexView(generic.ListView):
    model = Bar


class DetailView(generic.DetailView):
    model = Bar


class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Bar
    fields = ['name', 'address', 'category'] # '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)


class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Bar
    fields = ['name', 'address', 'category'] #'__all__'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('You do not have permission to edit.')
        return super(UpdateView, self).dispatch(request, *args, **kwargs)


class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Bar
    success_url = reverse_lazy('barmap:index')


class PersonalView(LoginRequiredMixin, generic.ListView):
    template_name = 'barmap/personal.html'
    model = Bar