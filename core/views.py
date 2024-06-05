from django.shortcuts import render
from clients.models import Client
from leads.models import Lead
def index(request):

    return render(request, 'core/index.html')

def search(request):
    query = request.GET.get('q', '')
    lead_object_list = Lead.objects.filter(name__icontains=query, converted_to_client=False,created_by=request.user)
    client_object_list = Client.objects.filter(name__icontains=query)
    return render(request, 'core/search.html',{'lead_object_list': lead_object_list, 'client_object_list': client_object_list})
def about(request):
    return render(request, 'core/about.html')