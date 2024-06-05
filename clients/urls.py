from django.urls import path
from .import views

app_name = 'clients'

urlpatterns = [
    path('', views.client_list, name='list'),
    path('<int:pk>/', views.client_details, name='details'),
    path('<int:pk>/edit/', views.clients_edit, name='edit'),
    path('<int:pk>/delete/', views.client_delete, name='delete'),
    path('add-client/', views.add_client, name='add'),
    path('export/', views.clients_export, name='export')
]