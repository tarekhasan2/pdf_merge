from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from pathlib import Path
from PyPDF2 import PdfFileMerger
import pdfplumber



def pdf_merge(request):
	if request.method == "POST":
		try:
			pdf_no_1 	= request.FILES['pdf1']
		except:
			pdf_no_1 	= None

		try:
			pdf_no_2 	= request.FILES['pdf2']
		except:
			pdf_no_2 	= None

		try:
			pdf_no_3 	= request.FILES['pdf3']
		except:
			pdf_no_3 	= None

		try:
			pdf_no_4 	= request.FILES['pdf4']
		except:
			pdf_no_4 	= None
		
		try:
			pdf_no_5 	= request.FILES['pdf5']
		except:
			pdf_no_5 	= None

		try:
			pdf_no_6 	= request.FILES['pdf6']
		except:
			pdf_no_6 	= None

		pdfs = [pdf_no_1,pdf_no_2, pdf_no_3, pdf_no_4, pdf_no_5, pdf_no_6]	


		output_pdf_name = request.POST.get('pdf_name')
		print(output_pdf_name)
		if not output_pdf_name:
			output_pdf_name = 'Final_pdf.pdf'
			
		if output_pdf_name.endswith(".pdf") or output_pdf_name.endswith(".PDF"): 
			output_pdf_name = output_pdf_name
		else:
			output_pdf_name = output_pdf_name + ".pdf"


		response = HttpResponse(content_type='text/pdf')
		response['Content-Disposition'] = 'attachment; filename={}'.format(output_pdf_name)

		

		merger = PdfFileMerger()
		for pdf in pdfs:
			if pdf:
				merger.append(pdf)
		
		merger.write(response)

		return response
		
		
	context = {}

	return render (request, "pdf_merge.html", context)
	



