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


class ArticleListView(ListView):

    model = drivetest
    # paginate_by = 100  # if pagination is desired
    template_name='drive/hola.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request):
        #today = date.today()
        pk=request.POST['key']
        pk=str(pk)
        # ref=referencia.objects.filter(refer=object.refer).order_by('-pk')[0]
        #
        # pais_busqueda=pais.objects.filter(pk=ref.pais).order_by('-pk')[0]
        # fabri=fabricante.objects.filter(pk=ref.fabricante).order_by('-pk')[0]
        # Nombre=fabricante_pais.objects.filter(pais=pais_busqueda, fabricante=fabri).order_by('-id')[0]

        document = Document()
        section = document.sections[0]
        header = section.header
        paragraph = header.paragraphs[0]
        run = paragraph.add_run()
        run.add_picture("sos.png")

        document.add_paragraph(
        pk, style='List Bullet'
        )
        document.save('salida.docx')

        return FileResponse(open('salida.docx', 'rb'), as_attachment=True, filename='hello.docx')


class DriveFormView(FormView):
    template_name = 'drive/holi.html'
    form_class = driveForm

    success_url ="/thanks/"

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)
