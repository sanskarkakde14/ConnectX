from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import csv
from django.http import HttpResponse
from teams.models import Team
from .models import Client
from .forms import AddClientForm

@login_required
def clients_export(request):
    team = request.user.userprofile.active_team
    clients = Client.objects.filter(created_by=request.user)
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="clients.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(['Client', 'Phone', 'Email', 'Address', 'Created At', 'Created By'])
    for client in clients:
        writer.writerow([client.name, client.phone, client.email, client.Address, client.created_at, client.created_by])
    return response


@login_required
def client_list(request):
    team = request.user.userprofile.active_team
    clients = Client.objects.filter(created_by=request.user)
    return render(request,'clients/clients_list.html', {'clients': clients})


@login_required
def client_delete(request, pk):
    team = request.user.userprofile.active_team
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    client.delete()
    messages.success(request, 'This Client was deleted')
    return redirect('clients:list')


@login_required
def clients_edit(request, pk):
    team = request.user.userprofile.active_team
    clients = get_object_or_404(Client, created_by=request.user, pk=pk)
    if request.method == 'POST':
        form = AddClientForm(request.POST, instance=clients)
        if form.is_valid():
            form.save()
            messages.success(request, 'This changes were saved')
            return redirect('clients:list')
    else:
        form = AddClientForm(instance=clients)
    return render(request, 'clients/clients_edit.html', {'form': form})


@login_required
def client_details(request, pk):
    team = request.user.userprofile.active_team
    client=get_object_or_404(Client, created_by=request.user,pk=pk)
    return render(request, 'clients/clients_details.html', {'client': client})

@login_required
def client_add_file(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    return redirect('clients:details', pk=pk)

@login_required
def add_client(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            team=Team.objects.filter(created_by=request.user)[0]
            client = form.save(commit=False)
            client.created_by = request.user
            client.team=request.user.userprofile.get_active_team()
            client.save()
            messages.success(request, 'This client was created')
            return redirect('dashboard:dashboard')
    else:
        form = AddClientForm()
    return render(request, 'clients/clients_add.html', {'form':form})














