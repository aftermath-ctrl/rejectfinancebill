from django.shortcuts import render

# Create your views here.



from django.views.generic import TemplateView

from django.core.files.storage import FileSystemStorage
import pdfplumber
import re
from recallmps.models import recall


# views.py


def home(request):
    recall_list = recall.objects.all()
    return render(request, 'home.html', {'recall_list': recall_list})

class HomePageView(TemplateView):
	template_name = 'home.html'


