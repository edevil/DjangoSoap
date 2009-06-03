from django.views.generic.simple import direct_to_template

from soaplib_handler import DjangoSoapApp, soapmethod, soap_types

class HelloWorldService(DjangoSoapApp):
    """My first SOAP WS in django"""
    
    __tns__ = "http://services.sapo.pt/ANDRE/"
    
    @soapmethod(soap_types.String, soap_types.Integer, _returns=soap_types.Array(soap_types.String))
    def say_hello(self, name, times):
        results = []
        for i in range(times):
            results.append("Hello %s" % name)
        return results

hello_world_service = HelloWorldService()
        
def index(request):
    """Just the homepage"""
    return direct_to_template(
            request,
            'index.html')
