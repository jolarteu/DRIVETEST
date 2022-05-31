from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from drive.views import *
app_name = "drive"


urlpatterns = [
    path('lista', ArticleListView.as_view(), name='lista'),
    path('agregar', DriveFormView.as_view(), name='agregar'),
    path('', views.CustomLoginView.as_view(), name='login'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
