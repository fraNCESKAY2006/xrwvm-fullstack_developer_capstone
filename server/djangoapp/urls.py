# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    path('get_cars', views.get_cars, name='getcars'),
]

# Only add static files serving in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
