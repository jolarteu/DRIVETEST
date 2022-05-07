from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from drive.views import *
app_name = "drive"


urlpatterns = [
    path('', DriveFormView.as_view(), name='article-list'),
]
