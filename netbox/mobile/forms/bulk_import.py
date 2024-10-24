from django.utils.translation import gettext_lazy as _
from netbox.forms import NetBoxModelImportForm
from utilities.forms.fields import DynamicModelChoiceField, CSVChoiceField
from dcim.models import Manufacturer, Platform, Region
from tenancy.models import Tenant
from circuits.models import Provider
from mobile.models import *
from mobile.choices import *

class MobileDeviceTypeImportForm(NetBoxModelImportForm):
    manufacturer = DynamicModelChoiceField(
        label=_('Manufacturer'),
        queryset=Manufacturer.objects.all(),
        to_field_name='name',
        help_text=_('The manufacturer which produces this device type')
    )
    default_platform = DynamicModelChoiceField(
        label=_('Default platform'),
        queryset=Platform.objects.all(),
        to_field_name='name',
        required=False,
        help_text=_('The default platform for devices of this type (optional)')
    )

    class Meta:
        model = MobileDeviceType
        fields = ('manufacturer', 'default_platform', 'model', 'part_number', 'description', 'comments', 'tags')

class MobileDeviceRoleImportForm(NetBoxModelImportForm):
    
    class Meta:
        model = MobileDeviceRole
        fields = ('name', 'color', 'description', 'tags')

class MobileDeviceImportForm(NetBoxModelImportForm):
    role = DynamicModelChoiceField(
        label=_('Device role'),
        queryset=MobileDeviceRole.objects.all(),
        to_field_name='name',
        help_text=_('Assigned role')
    )
    tenant = DynamicModelChoiceField(
        label=_('Tenant'),
        queryset=Tenant.objects.all(),
        required=False,
        to_field_name='name',
        help_text=_('Assigned tenant')
    )
    manufacturer = DynamicModelChoiceField(
        label=_('Manufacturer'),
        queryset=Manufacturer.objects.all(),
        to_field_name='name',
        help_text=_('Device type manufacturer')
    )
    device_type = DynamicModelChoiceField(
        label=_('Device type'),
        queryset=MobileDeviceType.objects.all(),
        to_field_name='model',
        help_text=_('Device type model')
    )
    platform = DynamicModelChoiceField(
        label=_('Platform'),
        queryset=Platform.objects.all(),
        required=False,
        to_field_name='name',
        help_text=_('Assigned platform')
    )
    status = CSVChoiceField(
        label=_('Status'),
        choices=MobileDeviceStatusChoices,
        help_text=_('Operational status')
    )

    class Meta:
        model = MobileDevice
        fields = ('name', 'role', 'tenant', 'manufacturer', 'device_type', 'platform', 'serial', 'asset_tag', 'status', 'description', 'comments', 'tags')

class MobileNumberImportForm(NetBoxModelImportForm):
    
    status = CSVChoiceField(
        label=_('Status'),
        choices=MobileNumberStatusChoices,
        required=False,
        initial=''
    )
    tenant = DynamicModelChoiceField(
        label=_('Tenant'),
        queryset=Tenant.objects.all(),
        required=True,
        to_field_name='name',
    )
    region = DynamicModelChoiceField(
        label=_('Region'),
        queryset=Region.objects.all(),
        required=False
    )
    provider = DynamicModelChoiceField(
        label=_('Provider'),
        queryset=Provider.objects.all(),
        required=False,    
    )
    
    forward_to = DynamicModelChoiceField(
        queryset=MobileNumber.objects.all(),
        required=False
    )
    
    class Meta:
        model = MobileNumber
        fields = ('number', 'status','tenant','region', 'provider', 'forward_to', 'description', 'comments')
        