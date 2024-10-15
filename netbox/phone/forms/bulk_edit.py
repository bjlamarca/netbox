from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import NetBoxModelBulkEditForm
from utilities.forms import add_blank_choice
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from dcim.models import Region
from circuits.models import Provider
from tenancy.models import Tenant
from phone.models import Number, NumberRole, NumberAssignment
from phone.choices import NumberStatusChoices
from utilities.forms.rendering import FieldSet

__all__ = (
    'NumberBulkEditForm',
    'NumberAssignmentBulkEditForm',
    'NumberRoleBulkEditForm',
)

class NumberBulkEditForm(NetBoxModelBulkEditForm):
    status = forms.ChoiceField(
        label=_('Status'),
        choices=add_blank_choice(NumberStatusChoices),
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
        queryset=Number.objects.all(),
        required=False
    )
    description = forms.CharField(
        max_length=200,
        required=False
    )
    comments = CommentField()
    
    model = Number
    fieldsets = (
            FieldSet('number', 'status','region', 'provider', 'forward_to', 'description', 'comments'),
        )
    nullable_fields = ('status','region', 'provider', 'forward_to', 'description', 'comments')

class NumberAssignmentBulkEditForm(NetBoxModelBulkEditForm):
    number = DynamicModelChoiceField(
        label=_('Number'),
        queryset=Number.objects.all(),
        required=False
    )
    role = DynamicModelChoiceField(
        label=_('Role'),
        queryset=NumberRole.objects.all(),
        required=False
    )

    model = NumberAssignment
    fieldsets = (
        FieldSet('id', 'object_type_id', 'object_id', 'number', 'role'),
    )
    nullable_fields = ('role', 'description',)

class NumberRoleBulkEditForm(NetBoxModelBulkEditForm):
    description = forms.CharField(
        label=_('Description'),
        max_length=200,
        required=False
    )

    model = NumberRole
    fieldsets = (
        FieldSet('description'),
    )
    nullable_fields = ('description',)
