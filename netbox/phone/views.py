from django.http import HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404
from core.models import ObjectType


from netbox.views import generic
from phone.models import *
from phone.tables import *
from phone.forms import model_forms, bulk_edit, bulk_import, filtersets
from phone.filtersets import *
from utilities.views import GetRelatedModelsMixin, ViewTab, register_model_view
from utilities.urls import get_model_urls
from tenancy.views import ObjectContactsView


@register_model_view(Number)
class NumberView(generic.ObjectView):
    queryset = Number.objects.all()

    def get_extra_context(self, request, instance):
        table = NumberAssignmentTable(instance.assignments.all())
        table.configure(request)
        table.columns.hide('number')

        return {
            'assignment_table': table,
        }


class NumberListView(generic.ObjectListView):
    queryset = Number.objects.all()
    filterset = NumberFilterSet
    filterset_form = filtersets.NumberFilterForm
    table = NumberTable   

@register_model_view(Number, 'edit')
class NumberEditView(generic.ObjectEditView):
    queryset = Number.objects.all()
    form = model_forms.NumberForm

@register_model_view(Number, 'delete')
class NumberDeleteView(generic.ObjectDeleteView):
    queryset = Number.objects.all()


class NumberBulkEditView(generic.BulkEditView):
    queryset = Number.objects.all()
    filterset = NumberFilterSet
    table = NumberTable
    form = bulk_edit.NumberBulkEditForm

class NumberBulkImportView(generic.BulkImportView):
    queryset = Number.objects.all()
    model_form=bulk_import.NumberImportForm

class NumberBulkDeleteView(generic.BulkDeleteView):
    queryset = Number.objects.all()
    filterset = NumberFilterSet
    table = NumberTable

#Number Assignment
@register_model_view(NumberAssignment)
class NumberAssignmentView(generic.ObjectView):
    queryset = NumberAssignment.objects.all()


class NumberAssignmentListView(generic.ObjectListView):
    queryset = NumberAssignment.objects.all()
    filterset = NumberAssignmentFilterSet
    filterset_form = filtersets.NumberAssignmentFilterForm
    table = NumberAssignmentTable
    template_name = 'phone/numberassignment_list.html'
   
@register_model_view(NumberAssignment, 'edit')
class NumberAssignmentEditView(generic.ObjectEditView):
    queryset = NumberAssignment.objects.all()
    form = model_forms.NumberAssignmentForm
    template_name='phone/numberassignment_edit.html'

    def alter_object(self, instance, request, url_args, url_kwargs):
        #If new instance, check where request came from
        
        if not instance.pk:
            caller = request.GET.get('caller')
            if caller == 'number':
                instance.number = get_object_or_404(Number, pk=request.GET.get('number')) 
            elif caller == 'panel':
                content_type = get_object_or_404(ContentType, pk=request.GET.get('object_type'))
                pk=request.GET.get('object_id')
                instance.object = get_object_or_404(content_type.model_class(), pk=pk)
                
        return instance

@register_model_view(NumberAssignment, 'delete')
class NumberAssignmentDeleteView(generic.ObjectDeleteView):
    queryset = NumberAssignment.objects.all()

class NumberAssignmentBulkEditView(generic.BulkEditView):
    queryset = NumberAssignment.objects.all()
    filterset = NumberAssignmentFilterSet
    table = NumberAssignmentTable
    form = bulk_edit.NumberAssignmentBulkEditForm

class NumberAssignmentBulkImportView(generic.BulkImportView):
    queryset = NumberAssignment.objects.all()
    model_form=bulk_import.NumberAssignmentImportForm

class NumberAssignmentBulkDeleteView(generic.BulkDeleteView):
    queryset = NumberAssignment.objects.all()
    filterset = NumberAssignmentFilterSet
    table = NumberAssignmentTable


class NumberAssignmentTestView(View):
    def post(self, request):
        from netbox.registry import registry
        # from django.contrib.contenttypes.models import ContentType
        # from django.db import models
        result = "<ul>"
        for item in registry['event_types'].items():
              result = result + '<li>' + str(item) + '</li>'
        
        # # queryset=ObjectType.objects.all()
        # # for item in queryset:
        # #     result = result + '<p>' + str(item) + str(item.id) + '</p>'
            
        result = result + '</ul>'
        # import datetime
        # from phone.jobs import MyHousekeepingJob
        # MyHousekeepingJob.enqueue(schedule_at=datetime.datetime(2024, 10, 18), )
        print("Hello")
        return HttpResponse(result, status=200)

#Number Role
@register_model_view(NumberRole)
class NumberRoleView(generic.ObjectView):
    queryset = NumberRole.objects.all()


class NumberRoleListView(generic.ObjectListView):
    queryset = NumberRole.objects.all()
    filterset = NumberRoleFilterSet
    filterset_form = filtersets.NumberRoleFilterForm
    table = NumberRoleTable   

@register_model_view(NumberRole, 'edit')
class NumberRoleEditView(generic.ObjectEditView):
    queryset = NumberRole.objects.all()
    form = model_forms.NumberRoleForm

@register_model_view(NumberRole, 'delete')
class NumberRoleDeleteView(generic.ObjectDeleteView):
    queryset = NumberRole.objects.all()


class NumberRoleBulkEditView(generic.BulkEditView):
    queryset = NumberRole.objects.all()
    filterset = NumberRoleFilterSet
    table = NumberRoleTable
    form = bulk_edit.NumberRoleBulkEditForm

class NumberRoleBulkImportView(generic.BulkImportView):
    queryset = NumberRole.objects.all()
    model_form=bulk_import.NumberRoleImportForm

class NumberRoleBulkDeleteView(generic.BulkDeleteView):
    queryset = NumberRole.objects.all()
    filterset = NumberRoleFilterSet
    table = NumberRoleTable


