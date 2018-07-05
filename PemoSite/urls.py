from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('',  RedirectView.as_view(url='/EA3/')),
    path('EA3/', include('EA3.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
