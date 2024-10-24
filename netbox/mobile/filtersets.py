import django_filters
from django.db.models import Q
from django.utils.translation import gettext as _
from netbox.filtersets import NetBoxModelFilterSet, OrganizationalModelFilterSet
from utilities.filters import TreeNodeMultipleChoiceFilter
from tenancy.models import Tenant, Contact
from tenancy.filtersets import TenancyFilterSet
from dcim.models import Region
from mobile.choices import *
from mobile.models import *
from dcim.models import Manufacturer, Platform
from circuits.models import Provider



class MobileDeviceTypeFilterSet(NetBoxModelFilterSet):
    manufacturer = django_filters.ModelMultipleChoiceFilter(
        queryset=Manufacturer.objects.all(),
        label=_('Manufacturer'),
    )
    default_platform = django_filters.ModelMultipleChoiceFilter(
        queryset=Platform.objects.all(),
        label=_('Default platform'),
    )

    class Meta:
        model = MobileDeviceType
        fields = ('id', 'model', 'part_number', 'description')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(manufacturer__name__icontains=value) |
            Q(model__icontains=value) |
            Q(part_number__icontains=value) |
            Q(description__icontains=value) |
            Q(comments__icontains=value)
        )
    
class MobileDeviceRoleFilterSet(OrganizationalModelFilterSet):
    print('Filter')
    class Meta:
        model = MobileDeviceRole
        fields = ('id', 'name', 'color', 'description')


class MobileDeviceFilterSet(NetBoxModelFilterSet):
    device_type = django_filters.ModelMultipleChoiceFilter(
        queryset=MobileDeviceType.objects.all(),
        label=_('Device type'),
    )
    role = django_filters.ModelMultipleChoiceFilter(
        queryset=MobileDeviceRole.objects.all(),
        label=_('Role'),
    )
    role_id = django_filters.ModelMultipleChoiceFilter(
        field_name='role_id',
        queryset=MobileDeviceRole.objects.all(),
        label=_('Role (ID)'),
    )
    contact = django_filters.ModelMultipleChoiceFilter(
        queryset=Contact.objects.all(),
        label=_('Contact')
    )
    platform = django_filters.ModelMultipleChoiceFilter(
        queryset=Platform.objects.all(),
        label=_('Platform'),
    )
    status = django_filters.MultipleChoiceFilter(
        choices=MobileDeviceStatusChoices,
        null_value=None
    )
    tenant = django_filters.ModelMultipleChoiceFilter(
        queryset=Tenant.objects.all(),
        field_name='tenant__id',
        to_field_name='id',
        label='Tenant (id)',
    )
    
    class Meta:
        model = MobileDevice
        fields = ('id', 'role', 'role_id', 'contact', 'tenant', 'asset_tag', 'description')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value)|
            Q(contact__name__icontains=value)|
            Q(tenant__name__icontains=value)|
            Q(serial__icontains=value.strip()) |
            Q(asset_tag__icontains=value.strip()) |
            Q(description__icontains=value.strip()) |
            Q(comments__icontains=value)
        )
    
class MobileNumberFilterSet(NetBoxModelFilterSet, TenancyFilterSet,):

    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )
    number = django_filters.ModelMultipleChoiceFilter(
        field_name='number',
        queryset=MobileNumber.objects.all(),
        to_field_name='number',
        label='number',
    )
    status = django_filters.MultipleChoiceFilter(
        choices=MobileNumberStatusChoices,
        null_value=None
    )
    contact = django_filters.ModelMultipleChoiceFilter(
        queryset=Contact.objects.all(),
        label=_('Contact')
    )
    tenant = django_filters.ModelMultipleChoiceFilter(
        queryset=Tenant.objects.all(),
        field_name='tenant__id',
        to_field_name='id',
        label='Tenant (id)',
    )
    region = TreeNodeMultipleChoiceFilter(
        queryset=Region.objects.all(),
        field_name='region__id',
        to_field_name='id',
        label='Region (id)',
    )
    provider = django_filters.ModelMultipleChoiceFilter(
        queryset=Provider.objects.all(),
        field_name='provider__id',
        to_field_name='id',
        label='Provider (id)',
    )
   

    class Meta():
        model = MobileNumber
        fields = ('number', 'status', 'contact', 'tenant', 'region', 'description', 'provider')

    def search(self, queryset, number, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(number__icontains=value)|
            Q(contact__name__icontains=value)|
            Q(tenant__name__icontains=value)|
            Q(region__name__icontains=value)|
            Q(description__icontains=value)|
            Q(provider__name__icontains=value)
        )