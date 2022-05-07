from django.shortcuts import render
from django.views.generic.edit import FormView
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from drive.forms import driveForm
from drive.models import drivetest

class ArticleListView(ListView):

    model = drivetest
    # paginate_by = 100  # if pagination is desired
    template_name='drive/hola.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DriveFormView(FormView):
    template_name = 'drive/holi.html'
    form_class = driveForm

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     form.save()
    #
    #     return super().form_valid(form)

    success_url ="/thanks/"

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)
