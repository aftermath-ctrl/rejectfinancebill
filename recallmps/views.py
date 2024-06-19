from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import recall
# views.py
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import pdfplumber
import re
from .models import recall
from .forms import PDFUploadForm


class MPListView(ListView):
	model = recall
	template_name = 'home.html'




def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['pdf_file']
            fs = FileSystemStorage()
            filename = fs.save(pdf_file.name, pdf_file)

            # Read the PDF file and extract data
            with pdfplumber.open(fs.path(filename)) as pdf:
                # Loop through each page and extract data
                for page in pdf.pages:
                    text = page.extract_text()
                    # Split the text into rows
                    rows = text.split('\n')
                    # Process each row and save the data to your Django models
                    for row in rows:
                        # Split the row into columns (assuming a fixed number of columns)
                        columns = re.split(r'\s+', row.strip(), maxsplit=2)
                        if len(columns) == 3:
                            name, constituency, _ = columns
                            # Save the data to your Django model
                            recall_obj = recall.objects.create(
                                name=name,
                                constituency=constituency
                            )

            return redirect('home')
    else:
        form = PDFUploadForm()

    return render(request, 'upload_pdf.html', {'form': form})