from django.contrib import admin
from .models import Client
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ClientResource(resources.ModelResource):
    class Meta:
        model=Client

class ClientAdmin(ImportExportModelAdmin):
    resource_class = ClientResource

admin.site.register(Client, ClientAdmin)

