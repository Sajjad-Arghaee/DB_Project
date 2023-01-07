from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

# first name is for route , the second one is for frontend
urlpatterns = [
    path('a', views.get_projects, name='aa'),
    path('b', views.get_projects2, name='aa2'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)