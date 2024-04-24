from django.shortcuts import render
import os
# Create your views here.
from django.http import HttpResponse

from Portfolio import settings

def home(request):
	return render(request,'home.html')

def project(request):
	return render(request,'project.html')

def contact(request):
	return render(request,'contact.html')

def crd(request):
     return render(request, 'Crime_Data_Visualization.html')

def gvds(request):
     return render(request, 'gvds.html')

def cen(request):
     return render(request, 'census.html')

from django.http import JsonResponse

import os
from django.http import JsonResponse
from Portfolio import settings

def fetch_file_content(request):
    file_name = request.GET.get('file', '')
    if file_name:
        file_path = os.path.join(settings.BASE_DIR, file_name)
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            return JsonResponse(content, safe=False)
        except FileNotFoundError:
            return JsonResponse("File not found", status=404, safe=False)
    else:
        return JsonResponse("File name not provided", status=400, safe=False)


import subprocess

def execute_script(request):
    script_path = request.GET.get('script', '')
    try:
        output = subprocess.check_output(['python', script_path], stderr=subprocess.STDOUT)
        return JsonResponse(output.decode('utf-8'), safe=False)
    except subprocess.CalledProcessError as e:
        return JsonResponse(str(e.output), status=500, safe=False)
    
