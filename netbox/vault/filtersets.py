import django_filters
from django.db.models import Q
from utilities.filters import ContentTypeFilter, TreeNodeMultipleChoiceFilter
from netbox.filtersets import NetBoxModelFilterSet, OrganizationalModelFilterSet
from vault.models import *

__all__ = [
    'PasswordFilterSet',
    'PasswordRoleFilterSet'
]

class PasswordFilterSet(NetBoxModelFilterSet):
    q = django_filters.CharFilter(
            method='search',
            label='Search',
        )
    object_type = ContentTypeFilter()
    role = django_filters.ModelMultipleChoiceFilter(
        field_name='role__slug',
        queryset=PasswordRole.objects.all(),
        to_field_name='slug',
        label='Password Role',
    )

    class Meta():
        model = Password
        fields =('id', 'object_type_id', 'object_id', 'username', 'role','description',)

    def search(self, queryset, username, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(username__icontains=value)|
            Q(role__name__icontains=value)|
            Q(description__icontains=value)|
            Q(comments__icontains=value),
        )
    

class PasswordRoleFilterSet(OrganizationalModelFilterSet):

    class Meta:
        model = PasswordRole
        fields = ('id', 'name', 'description')