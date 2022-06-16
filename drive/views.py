import os
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView, UpdateView, DeleteView
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from drive.forms import driveForm, FacturaUpdateForm
from drive.models import drivetest
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from django.http import FileResponse
from map import main_map
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class CustomLoginView(LoginView):
    template_name = 'drive/login.html'

    redirect_authenticated_user = True

#prueba


class ArticleListView(ListView):
    model = drivetest
    template_name='drive/table.html'
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['static']=str(settings.STATIC_ROOT)
        return context

    def post(self, request):

        #today = date.today()

        pk=request.POST['key']
        name=request.POST['name']


        try:
            main_map(pk)


            return FileResponse(open(os.path.join(settings.STATIC_ROOT, 'demo.docx'), 'rb'), as_attachment=True, filename='informe_'+str(name)+'.docx')

        except Exception as e:
            print(e)
            return FileResponse(open(os.path.join(settings.STATIC_ROOT, 'salida.docx'), 'rb'), as_attachment=True, filename='informe_'+str(name)+'.docx')


class DriveFormView(FormView):
    template_name = 'drive/agregar.html'
    form_class = driveForm
    success_url ="/"

    def form_valid(self, form):
        """Save form data."""
        app_model = form.save(commit=False)
        #app_model.user = self.request.user
        app_model.user = User.objects.get(username=self.request.user)
        app_model.save()
        #form.save()
        return super().form_valid(form)

    def get_queryset(self):
        return User.objects.filter(user=self.request.user)

class  FacturaUpdateView(UpdateView):
    model=drivetest
    template_name='drive/update.html'
    form_class=FacturaUpdateForm
    success_url=reverse_lazy('drive:lista')

class DriveDelete(DeleteView):
    model = drivetest
    success_url ="/"

    # def get_queryset(self):
    #     return User.objects.filter(username=self.request.user)

    def get_context_data(self, **kwargs):
        #user=get_queryset()
        self.object = self.get_object()
        usario=User.objects.get(username=self.object.user)
        context = super().get_context_data(**kwargs)
        # if self.object.user == self.request.user:
        context['usuario'] = usario
        # else:
        context['titulo']='holii'

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == self.request.user:
            success_url = self.get_success_url()
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        else:

            return HttpResponseRedirect(self.success_url)
