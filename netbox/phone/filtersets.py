
import django_filters
from django.db.models import Q
from django.utils.translation import gettext as _

from netbox.filtersets import NetBoxModelFilterSet, OrganizationalModelFilterSet
from utilities.filters import ContentTypeFilter, TreeNodeMultipleChoiceFilter
from phone.models import *
from tenancy.filtersets import TenancyFilterSet, ContactModelFilterSet
from tenancy.models import Tenant
from dcim.models import Region
from circuits.models import Provider

class NumberFilterSet(NetBoxModelFilterSet, TenancyFilterSet,):

    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )
    number = django_filters.ModelMultipleChoiceFilter(
        field_name='number',
        queryset=Number.objects.all(),
        to_field_name='number',
        label='number',
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
        label='Region (id)',
    )
    forward_to = django_filters.ModelMultipleChoiceFilter(
        field_name='forward_to__id',
        queryset=Number.objects.all(),
        to_field_name='id',
        label='Forward To (id)',
    )
    

    class Meta():
        model = Number
        fields = ('number', 'status', 'tenant', 'region', 'description', 'provider', 'forward_to')

    def search(self, queryset, number, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(number__icontains=value)|
            Q(tenant__name__icontains=value)|
            Q(region__name__icontains=value)|
            Q(description__icontains=value)|
            Q(provider__name__icontains=value)|
            Q(forward_to__number__icontains=value)
        )

class NumberAssignmentFilterSet(NetBoxModelFilterSet):

    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )
    object_type = ContentTypeFilter()
    number = django_filters.ModelMultipleChoiceFilter(
        field_name='number',
        queryset=Number.objects.all(),
        to_field_name='number',
        label='number',
    )
    role = django_filters.ModelMultipleChoiceFilter(
        field_name='role__slug',
        queryset=NumberRole.objects.all(),
        to_field_name='slug',
        label=_('Contact role (slug)'),
    )

    class Meta():
        model = NumberAssignment
        fields =(('id', 'object_type_id', 'object_id', 'number', 'role'))

    def search(self, queryset, number, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(number__number__icontains=value)|
            Q(role__name__icontains=value)
        )
    
class NumberRoleFilterSet(OrganizationalModelFilterSet):

    class Meta:
        model = NumberRole
        fields = ('id', 'name', 'description')