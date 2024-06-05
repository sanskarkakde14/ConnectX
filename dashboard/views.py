from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from leads.models import Lead
from clients.models import Client
from teams.models import Team
@login_required
def dashboard(request):
    team = request.user.userprofile.get_active_team()
    leads = Lead.objects.filter(team=team,created_by=request.user).order_by('-created_at')[0:5]
    clients = Client.objects.filter(team=team,created_by=request.user).order_by('-created_at')[0:5]
    lead_count = Lead.objects.filter(converted_to_client=False,created_by=request.user,team=team).count()
    client_count = Client.objects.filter(team=team, created_by=request.user).count()
    leadtoclient_count = Lead.objects.filter(converted_to_client=True,created_by=request.user,team=team).count()
    plot = Lead.objects.filter(property_type='plot',converted_to_client=False,created_by=request.user,team=team).count()
    apartment = Lead.objects.filter(property_type='apartment',converted_to_client=False,created_by=request.user,team=team).count()
    readytomove = Lead.objects.filter(property_type='readyTomove',converted_to_client=False,created_by=request.user,team=team).count()
    property_type_label = ['Plot' ,'Apartment', 'ReadyToMove']
    property_type = [plot,apartment,readytomove]
    low = Lead.objects.filter(priority='low',converted_to_client=False,created_by=request.user,team=team).count()
    high = Lead.objects.filter(priority='high',converted_to_client=False,created_by=request.user,team=team).count()
    medium = Lead.objects.filter(priority='medium',converted_to_client=False,created_by=request.user,team=team).count()
    priority_label = ['Low', 'High', 'Medium']
    priority = [low, high, medium]
    data=[]
    if request.GET.get('readyTomove'):
        print('user clicked summary')
        data = Lead.objects.filter(property_type='readyTomove',converted_to_client=False,team=team)

    data1 = []
    if request.GET.get('plot'):
        print('user clicked summary')
        data1 = Lead.objects.filter(property_type='plot', converted_to_client=False, team=team)

    data2 = []
    if request.GET.get('apartment'):
        print('user clicked summary')
        data2 = Lead.objects.filter(property_type='apartment', converted_to_client=False, team=team)

    return render(request,'dashboard/dashboard.html', {'leads':leads, 'clients':clients, 'lead_count':lead_count,
                                                       'client_count':client_count,'leadtoclient_count':leadtoclient_count,
                                                       'property_type_label':property_type_label, 'property_type':property_type,
                                                       'priority_label':priority_label, 'priority':priority,"data":data,
                                                       "data1":data1,"data2":data2})

