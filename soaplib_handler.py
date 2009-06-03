# soaplib_handler.py

from soaplib.wsgi_soap import SimpleWSGISoapApp
from soaplib.service import soapmethod
from soaplib.serializers import primitive as soap_types

from django.http import HttpResponse

class DjangoSoapApp(SimpleWSGISoapApp):

    def __call__(self, request):
        django_response = HttpResponse()
        def start_response(status, headers):
            status, reason = status.split(' ', 1)
            django_response.status_code = int(status)
            for header, value in headers:
                django_response[header] = value
        response = super(DjangoSoapApp, self).__call__(request.META, start_response)
        django_response.content = "\n".join(response)

        return django_response
