
from utilities.views import GetRelatedModelsMixin, ViewTab, register_model_view
from netbox.views import generic
from mobile.models import *
from mobile.tables import *
from mobile.forms import model_forms, bulk_edit, bulk_import, filtersets
from mobile.filtersets import *

#
# Device types
#

class MobileDeviceTypeListView(generic.ObjectListView):
    queryset = MobileDeviceType.objects.all()
    filterset = MobileDeviceTypeFilterSet
    filterset_form = filtersets.MobileDeviceTypeFilterForm
    table = MobileDeviceTypeTable


@register_model_view(MobileDeviceType)
class MobileDeviceTypeView(GetRelatedModelsMixin, generic.ObjectView):
    queryset = MobileDeviceType.objects.all()

@register_model_view(MobileDeviceType, 'edit')
class MobileDeviceTypeEditView(generic.ObjectEditView):
    queryset = MobileDeviceType.objects.all()
    form = model_forms.MobileDeviceTypeForm


@register_model_view(MobileDeviceType, 'delete')
class MobileDeviceTypeDeleteView(generic.ObjectDeleteView):
    queryset = MobileDeviceType.objects.all()

class MobileDeviceTypeImportView(generic.BulkImportView):
    queryset = MobileDeviceType.objects.all()
    model_form = bulk_import.MobileDeviceTypeImportForm

class MobileDeviceTypeBulkEditView(generic.BulkEditView):
    queryset = MobileDeviceType.objects.all()
    filterset = MobileDeviceTypeFilterSet
    table = MobileDeviceTypeTable
    form = bulk_edit.MobileDeviceTypeBulkEditForm


class MobileDeviceTypeBulkDeleteView(generic.BulkDeleteView):
    queryset = MobileDeviceType.objects.all()
    filterset = MobileDeviceTypeFilterSet
    table = MobileDeviceTypeTable



#
# Device roles
#

class MobileDeviceRoleListView(generic.ObjectListView):
    queryset = MobileDeviceRole.objects.all()
    filterset = MobileDeviceRoleFilterSet
    filterset_form = filtersets.MobileDeviceRoleFilterForm
    table = MobileDeviceRoleTable


@register_model_view(MobileDeviceRole)
class MobileDeviceRoleView(GetRelatedModelsMixin, generic.ObjectView):
    queryset = MobileDeviceRole.objects.all()

@register_model_view(MobileDeviceRole, 'edit')
class MobileDeviceRoleEditView(generic.ObjectEditView):
    queryset = MobileDeviceRole.objects.all()
    form = model_forms.MobileDeviceRoleForm


@register_model_view(MobileDeviceRole, 'delete')
class MobileDeviceRoleDeleteView(generic.ObjectDeleteView):
    queryset = MobileDeviceRole.objects.all()


class MobileDeviceRoleBulkImportView(generic.BulkImportView):
    queryset = MobileDeviceRole.objects.all()
    model_form = bulk_import.MobileDeviceRoleImportForm


class MobileDeviceRoleBulkEditView(generic.BulkEditView):
    queryset = MobileDeviceRole.objects.all()
    filterset = MobileDeviceRoleFilterSet
    table = MobileDeviceRoleTable
    form = bulk_edit.MobileDeviceRoleBulkEditForm


class MobileDeviceRoleBulkDeleteView(generic.BulkDeleteView):
    queryset = MobileDeviceRole.objects.all()
    filterset = MobileDeviceRoleFilterSet
    table = MobileDeviceRoleTable


#
# Devices
#

class MobileDeviceListView(generic.ObjectListView):
    queryset = MobileDevice.objects.all()
    filterset = MobileDeviceFilterSet
    filterset_form = filtersets.MobileDeviceFilterForm
    table = MobileDeviceTable
    #template_name = 'dcim/device_list.html'
    


@register_model_view(MobileDevice)
class MobileDeviceView(generic.ObjectView):
    queryset = MobileDevice.objects.all()

@register_model_view(MobileDevice, 'edit')
class MobileDeviceEditView(generic.ObjectEditView):
    queryset = MobileDevice.objects.all()
    form = model_forms.MobileDeviceForm
    #template_name = 'dcim/device_edit.html'


@register_model_view(MobileDevice, 'delete')
class MobileDeviceDeleteView(generic.ObjectDeleteView):
    queryset = MobileDevice.objects.all()

class MobileDeviceBulkImportView(generic.BulkImportView):
    queryset = MobileDevice.objects.all()
    model_form = bulk_import.MobileDeviceImportForm


class MobileDeviceBulkEditView(generic.BulkEditView):
    queryset = MobileDevice.objects.all()
    filterset = MobileDeviceFilterSet
    table = MobileDeviceTable
    form = bulk_edit.MobileDeviceTypeBulkEditForm


class MobileDeviceBulkDeleteView(generic.BulkDeleteView):
    queryset = MobileDevice.objects.all()
    filterset = MobileDeviceFilterSet
    table = MobileDeviceTable


class MobileDeviceBulkRenameView(generic.BulkRenameView):
    queryset = MobileDevice.objects.all()
    filterset = MobileDeviceFilterSet
    table = MobileDeviceTable

#
# Devices
#

@register_model_view(MobileNumber)
class MobileNumberView(generic.ObjectView):
    queryset = MobileNumber.objects.all()

class MobileNumberListView(generic.ObjectListView):
    queryset = MobileNumber.objects.all()
    filterset = MobileNumberFilterSet
    filterset_form = filtersets.MobileNumberFilterForm
    table = MobileNumberTable   

@register_model_view(MobileNumber, 'edit')
class MobileNumberEditView(generic.ObjectEditView):
    queryset = MobileNumber.objects.all()
    form = model_forms.MobileNumberForm

@register_model_view(MobileNumber, 'delete')
class MobileNumberDeleteView(generic.ObjectDeleteView):
    queryset = MobileNumber.objects.all()


class MobileNumberBulkEditView(generic.BulkEditView):
    queryset = MobileNumber.objects.all()
    filterset = MobileNumberFilterSet
    table = MobileNumberTable
    form = bulk_edit.MobileNumberBulkEditForm

class MobileNumberBulkImportView(generic.BulkImportView):
    queryset = MobileNumber.objects.all()
    model_form=bulk_import.MobileNumberImportForm

class MobileNumberBulkDeleteView(generic.BulkDeleteView):
    queryset = MobileNumber.objects.all()
    filterset = MobileNumberFilterSet
    table = MobileNumberTable