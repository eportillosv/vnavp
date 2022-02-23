from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', views.index, name='index'),
    path('user', views.usuario, name='usuario'),
    path('user/crear', views.crear, name='crear'),
    path('user/edit', views.edit, name='edit'),
    path('user/<int:id>', views.delete, name='delete'),
    path('user/edit/<int:id>', views.edit, name='edit'),
]+ static(settings.MEDIA_URL, settings.STATIC_URL, document_root=settings.MEDIA_ROOT, document_root=settings.STATIC_ROOT )