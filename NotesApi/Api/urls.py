from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('notesapi/', NotesAPILP),
    
    path('notesapi/<int:pk>', NotesAPIRUD),

    path('auth/', include('rest_framework.urls', namespace='rest_framework'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
