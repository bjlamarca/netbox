
from django.utils.translation import gettext_lazy as _
from netbox.forms import NetBoxModelForm
from utilities.forms.fields import DynamicModelChoiceField, CommentField
from dcim.models import Manufacturer, Platform
from mobile.models import *
from tenancy.forms import TenancyForm

__all__=(
    'MobileDeviceTypeForm',
    'MobileDeviceRoleForm',
    'MobileDeviceForm',
    'MobileNumberForm',
)

class MobileDeviceTypeForm(NetBoxModelForm):
    manufacturer = DynamicModelChoiceField(
        label=_('Manufacturer'),
        queryset=Manufacturer.objects.all()
    )
    default_platform = DynamicModelChoiceField(
        label=_('Default platform'),
        queryset=Platform.objects.all(),
        required=False,
        selector=True,
    )
    comments = CommentField()

    class Meta:
        model = MobileDeviceType
        fields = ('manufacturer', 'model', 'default_platform', 'part_number', 'description', 'comments', 'tags')


class MobileDeviceRoleForm(NetBoxModelForm):
    
    class Meta:
        model = MobileDeviceRole
        fields = ('name', 'color', 'description', 'tags')

class MobileDeviceForm(TenancyForm, NetBoxModelForm):
   
    comments = CommentField()

    class Meta:
        model = MobileDevice
        fields = ('name', 'status', 'role', 'device_type', 'contact', 'tenant_group', 'tenant', 'serial', 'asset_tag', 'description', 'comments', 'tags')

class MobileNumberForm(TenancyForm, NetBoxModelForm):
    comments = CommentField()
    
    class Meta:
        model = MobileNumber
        fields = ('number', 'status', 'contact', 'device', 'provider', 'tenant_group', 'tenant',  'region', 'description', 'forward_to', 'tags', 'comments')