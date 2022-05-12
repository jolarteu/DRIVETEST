from django.shortcuts import render
from django.views.generic.edit import FormView
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from drive.forms import driveForm
from drive.models import drivetest
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from django.http import FileResponse
from map import main_map
from django.conf import settings


class ArticleListView(ListView):

    model = drivetest
    # paginate_by = 100  # if pagination is desired
    template_name='drive/table.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request):

        #today = date.today()

        pk=request.POST['key']
        name=request.POST['name']


        try:
            main_map(pk)

            return FileResponse(open('demo.docx', 'rb'), as_attachment=True, filename='informe_'+str(name)+'.docx')

        except Exception as e:
            print(e)
            return FileResponse(open('salida.docx', 'rb'), as_attachment=True, filename='informe_'+str(name)+'.docx')


class DriveFormView(FormView):
    template_name = 'drive/agregar.html'
    form_class = driveForm

    success_url ="/"

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)
