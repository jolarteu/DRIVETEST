from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from drive.views import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login
from django.views.static import serve
from django.urls import re_path
app_name = "drive"


urlpatterns = [
    path('', login_required(ArticleListView.as_view()), name='lista'),
    path('agregar', login_required(DriveFormView.as_view()), name='agregar'),
    path('accounts/login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', login_required(logout_then_login), name='logout'),
    path('editar/<int:pk>',login_required(FacturaUpdateView.as_view()), name='editar'),
    path('<pk>/delete/', login_required(DriveDelete.as_view()), name='eliminar'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
