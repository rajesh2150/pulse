from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Your API URLs
    path('', TemplateView.as_view(template_name='index.html')),  # Catch-all for React
]


