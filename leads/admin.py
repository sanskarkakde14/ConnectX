from django.contrib import admin
from .models import Lead
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class LeadResource(resources.ModelResource):
    class Meta:
        model=Lead

class LeadAdmin(ImportExportModelAdmin):
    resource_class = LeadResource

admin.site.register(Lead, LeadAdmin)



