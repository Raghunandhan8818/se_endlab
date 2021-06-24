from django.shortcuts import render
from django.urls import reverse_lazy

from exam.models import *
from exam.forms import *
from django.views.generic.edit import CreateView


# Create your views here.
class ExamCreate(CreateView):
    model = FirstModel
    form_class = ExamForm
    template_name = 'exam_form.html'
    success_message = 'Form Saved Successfully!!!!'
    success_url = reverse_lazy('home')


def home(request):
    return render(request, 'home.html')
