from django import forms
from django.utils.translation import gettext_lazy as _
from netbox.forms import NetBoxModelBulkEditForm
from utilities.forms import BulkEditForm, add_blank_choice
from utilities.forms.fields import DynamicModelChoiceField, CommentField, ColorField
from utilities.forms.rendering import FieldSet
from dcim.models import Manufacturer, Platform, Region
from tenancy.models import Tenant
from circuits.models import Provider
from mobile.models import *
from mobile.choices import *

__all__ = (
    'MobileDeviceTypeBulkEditForm',
    'MobileDeviceRoleBulkEditForm',
    'MobileDeviceBulkEditForm',
    '',
)

class MobileDeviceTypeBulkEditForm(NetBoxModelBulkEditForm):
    manufacturer = DynamicModelChoiceField(
        label=_('Manufacturer'),
        queryset=Manufacturer.objects.all(),
        required=False
    )
    default_platform = DynamicModelChoiceField(
        label=_('Default platform'),
        queryset=Platform.objects.all(),
        required=False
    )
    part_number = forms.CharField(
        label=_('Part number'),
        required=False
    )
    description = forms.CharField(
        label=_('Description'),
        max_length=200,
        required=False
    )
    comments = CommentField()

    model = MobileDeviceType
    fieldsets = (
        FieldSet('manufacturer', 'default_platform', 'part_number', name=_('Device Type'))
        
    )
    nullable_fields = ('part_number', 'description', 'comments')

class MobileDeviceRoleBulkEditForm(NetBoxModelBulkEditForm):
    color = ColorField(
        label=_('Color'),
        required=False
    )
    description = forms.CharField(
        label=_('Description'),
        max_length=200,
        required=False
    )

    model = MobileDeviceRole
    fieldsets = (
        FieldSet('color', 'description'),
    )
    nullable_fields = ('color', 'description')

class MobileDeviceBulkEditForm(NetBoxModelBulkEditForm):
    manufacturer = DynamicModelChoiceField(
        label=_('Manufacturer'),
        queryset=Manufacturer.objects.all(),
        required=False
    )
    device_type = DynamicModelChoiceField(
        label=_('Device type'),
        queryset=MobileDeviceType.objects.all(),
        required=False,
    )
    role = DynamicModelChoiceField(
        label=_('Device role'),
        queryset=MobileDeviceRole.objects.all(),
        required=False
    )
    tenant = DynamicModelChoiceField(
        label=_('Tenant'),
        queryset=Tenant.objects.all(),
        required=False
    )
    platform = DynamicModelChoiceField(
        label=_('Platform'),
        queryset=Platform.objects.all(),
        required=False
    )
    status = forms.ChoiceField(
        label=_('Status'),
        choices=add_blank_choice(MobileDeviceStatusChoices),
        required=False
    )
    serial = forms.CharField(
        max_length=50,
        required=False,
        label=_('Serial Number')
    )
    description = forms.CharField(
        label=_('Description'),
        max_length=200,
        required=False
    )
    comments = CommentField()

    model = MobileDevice
    fieldsets = (
        FieldSet('role', 'status', 'tenant', 'platform', 'description', name=_('Device')),
        FieldSet('manufacturer', 'serial', name=_('Hardware')),
    )
    nullable_fields = (
        'location', 'tenant', 'platform', 'serial', 'description', 'comments',
    )

class MobileNumberBulkEditForm(NetBoxModelBulkEditForm):
    status = forms.ChoiceField(
        label=_('Status'),
        choices=add_blank_choice(MobileNumberStatusChoices),
        required=False,
        initial=''
    )
    tenant = DynamicModelChoiceField(
        label=_('Tenant'),
        queryset=Tenant.objects.all(),
        required=False
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
    forward_to = forms.ModelChoiceField(
        label=_('Forward To'),
        queryset=MobileNumber.objects.all(),
        required=False
    )
    description = forms.CharField(
        max_length=200,
        required=False
    )
    comments = CommentField()
    
    model = MobileNumber
    fieldsets = (
            FieldSet('number', 'status','region', 'provider', 'forward_to', 'description', 'comments'),
        )
    nullable_fields = ('status','region', 'provider', 'forward_to', 'description', 'comments')