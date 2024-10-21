from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from utilities.views import GetRelatedModelsMixin, ViewTab, register_model_view
from netbox.views import generic
from vault.models import *
from vault.filtersets import *
from vault.forms import model_forms, bulk_edit, bulk_import, filtersets
from vault.tables import *


@register_model_view(Password)
class PasswordView(generic.ObjectView):
    queryset = Password.objects.all()

   
class PasswordListView(generic.ObjectListView):
    queryset = Password.objects.all()
    filterset = PasswordFilterSet
    filterset_form = filtersets.PasswordFilterForm
    table = PasswordTable   

@register_model_view(Password, 'edit')
class PasswordEditView(generic.ObjectEditView):
    queryset = Password.objects.all()
    form = model_forms.PasswordForm
    template_name='vault/password_edit.html'

    def alter_object(self, instance, request, url_args, url_kwargs):
               
        if not instance.pk:
            # Assign the assigned_object based on the URL parameters
            content_type = get_object_or_404(ContentType, pk=request.GET.get('object_type'))
            instance.object = get_object_or_404(
                content_type.model_class(),
                pk=request.GET.get('object_id'),
            )
               
        return instance

@register_model_view(Password, 'delete')
class PasswordDeleteView(generic.ObjectDeleteView):
    queryset = Password.objects.all()


class PasswordBulkEditView(generic.BulkEditView):
    queryset = Password.objects.all()
    filterset = PasswordFilterSet
    table = PasswordTable
    form = bulk_edit.PasswordBulkEditForm

class PasswordBulkImportView(generic.BulkImportView):
    queryset = Password.objects.all()
    model_form=bulk_import.PasswordBulkImportForm

class PasswordBulkDeleteView(generic.BulkDeleteView):
    queryset = Password.objects.all()
    filterset = PasswordFilterSet
    table = PasswordTable


#Password Role
@register_model_view(PasswordRole)
class PasswordRoleView(generic.ObjectView):
    queryset = PasswordRole.objects.all()


class PasswordRoleListView(generic.ObjectListView):
    queryset = PasswordRole.objects.all()
    filterset = PasswordRoleFilterSet
    filterset_form = filtersets.PasswordRoleFilterForm
    table = PasswordRoleTable   

@register_model_view(PasswordRole, 'edit')
class PasswordRoleEditView(generic.ObjectEditView):
    queryset = PasswordRole.objects.all()
    form = model_forms.PasswordRoleForm

@register_model_view(PasswordRole, 'delete')
class PasswordRoleDeleteView(generic.ObjectDeleteView):
    queryset = PasswordRole.objects.all()


class PasswordRoleBulkEditView(generic.BulkEditView):
    queryset = PasswordRole.objects.all()
    filterset = PasswordRoleFilterSet
    table = PasswordRoleTable
    form = bulk_edit.PasswordRoleBulkEditForm

class PasswordRoleBulkImportView(generic.BulkImportView):
    queryset = PasswordRole.objects.all()
    model_form=bulk_import.PasswordRoleImportForm

class PasswordRoleBulkDeleteView(generic.BulkDeleteView):
    queryset = PasswordRole.objects.all()
    filterset = PasswordRoleFilterSet
    table = PasswordRoleTable