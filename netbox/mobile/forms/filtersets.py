from django import forms
from django.utils.translation import gettext_lazy as _
from netbox.forms import NetBoxModelFilterSetForm
from utilities.forms.fields import ColorField, DynamicModelMultipleChoiceField, TagFilterField
from dcim.models import Manufacturer, Platform, Region
from tenancy.models import Tenant
from circuits.models import Provider
from mobile.models import *
from mobile.choices import *

__all__=(
    'MobileDeviceTypeFilterForm',
    'MobileDeviceRoleFilterForm',
    'MobileDeviceFilterForm',
    'MobileNumberFilterForm',
)


class MobileDeviceTypeFilterForm(NetBoxModelFilterSetForm):
    model = MobileDeviceType
    manufacturer = DynamicModelMultipleChoiceField(
        queryset=Manufacturer.objects.all(),
        required=False,
        label=_('Manufacturer')
    )
    default_platform = DynamicModelMultipleChoiceField(
        queryset=Platform.objects.all(),
        required=False,
        label=_('Default platform')
    )
    part_number = forms.CharField(
        label=_('Part number'),
        required=False
    )
    tag = TagFilterField(model)

class MobileDeviceRoleFilterForm(NetBoxModelFilterSetForm):
    model = MobileDeviceRole
    tag = TagFilterField(model)

class MobileDeviceFilterForm(NetBoxModelFilterSetForm):
    model = MobileDevice
    manufacturer = DynamicModelMultipleChoiceField(
        queryset=Manufacturer.objects.all(),
        required=False,
        label=_('Manufacturer')
    )
    device_type = DynamicModelMultipleChoiceField(
        queryset=MobileDeviceType.objects.all(),
        required=False,
        label=_('Model')
    )
    platform = DynamicModelMultipleChoiceField(
        queryset=Platform.objects.all(),
        required=False,
        null_option='None',
        label=_('Platform')
    )
    status = forms.MultipleChoiceField(
        label=_('Status'),
        choices=MobileDeviceStatusChoices,
        required=False
    )
    serial = forms.CharField(
        label=_('Serial'),
        required=False
    )
    asset_tag = forms.CharField(
        label=_('Asset tag'),
        required=False
    )
    tag = TagFilterField(model)

class MobileNumberFilterForm(NetBoxModelFilterSetForm):

    model = MobileNumber
    status = forms.MultipleChoiceField(
        label=_('Status'),
        choices=MobileNumberStatusChoices,
        required=False
    )
    tenant = DynamicModelMultipleChoiceField(
        queryset=Tenant.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
    )
    region = DynamicModelMultipleChoiceField(
        queryset=Region.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
    )
    provider = DynamicModelMultipleChoiceField(
        queryset=Provider.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
    )
    tag = TagFilterField(model)