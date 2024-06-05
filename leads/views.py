from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from clients.models import Client
from teams.models import Team
from .models import Lead
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class LeadListView(LoginRequiredMixin, ListView):
    model = Lead
    def get_queryset(self):
        queryset = super(LeadListView, self).get_queryset()
        team = self.request.user.userprofile.active_team
        return queryset.filter(team=team,converted_to_client=False)
                                        #created_by=self.request.user,

class LeadDetailView(LoginRequiredMixin, DetailView):
    model = Lead

    def get_queryset(self):
        queryset = super(LeadDetailView, self).get_queryset()
        team = self.request.user.userprofile.active_team
        return queryset.filter(team=team, pk=self.kwargs.get('pk'))


class LeadDeleteView(LoginRequiredMixin, DeleteView):
    model = Lead
    success_url = reverse_lazy('leads:list')
    def get_queryset(self):
        queryset = super(LeadDeleteView, self).get_queryset()
        team = self.request.user.userprofile.active_team
        return queryset.filter(team=team, pk=self.kwargs.get('pk'))
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class LeadUpdateView(LoginRequiredMixin, UpdateView):
    model = Lead
    fields = ('name', 'email', 'phone', 'Address', 'property_price', 'property_size', 'property_locality', 'property_type', 'priority')
    success_url = reverse_lazy('leads:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Lead'
        return context

    def get_queryset(self):
        queryset = super(LeadUpdateView, self).get_queryset()
        team = self.request.user.userprofile.active_team
        return queryset.filter(team=team, pk=self.kwargs.get('pk'))


class LeadCreateView(LoginRequiredMixin, CreateView):
    model = Lead
    fields = ('name', 'email', 'phone', 'Address', 'property_price', 'property_size', 'property_locality', 'property_type', 'priority')
    success_url = reverse_lazy('leads:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team = self.request.user.userprofile.get_active_team()
        context['team'] = team
        context['title'] = 'Add Lead'
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.team = self.request.user.userprofile.get_active_team()
        self.object.save()
        return redirect(self.get_success_url())



class ConvertToClientView(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
        team = self.request.user.userprofile.get_active_team()
        client = Client.objects.create(
                name=lead.name,
                email=lead.email,
                phone=lead.phone,
                Address=lead.Address,
                property_price=lead.property_price,
                property_size=lead.property_size,
                property_locality=lead.property_locality,
                property_type=lead.property_type,
                priority=lead.priority,
                created_by=request.user,
                team=team
            )
        lead.converted_to_client = True
        lead.save()
        messages.success(request, 'This lead was converted to client')
        return redirect('leads:list')



