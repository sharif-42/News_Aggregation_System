from django.http import HttpResponse
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .resources import NewsResources

def import_export_data(request):
        person_resource = NewsResources()
        dataset = person_resource.export()
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="persons.csv"'
        #return Response({'h1':h1,'h2':h2}, status=status.HTTP_200_OK)
        return response

