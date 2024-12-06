from django.http import HttpResponse
from django.template import loader

def gerenciarpratos(request):
    template = loader.get_template('gerenciarpratos.html')
    return HttpResponse(template.render())