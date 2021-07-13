from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bar/', include('bar.urls')),
    path('', RedirectView.as_view(url='/barmap/')),
    path('barmap/', include('barmap.urls')),
]
