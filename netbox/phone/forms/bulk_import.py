from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import NetBoxModelImportForm
from phone.models import *
from phone.choices import *
from tenancy.models import Tenant
from circuits.models import Provider
from dcim.models import Region
from utilities.forms.fields import CommentField, DynamicModelChoiceField, CSVContentTypeField, CSVModelChoiceField
from utilities.forms.rendering import FieldSet


__all__ = (
    'NumberImportForm',
    'NumberAssignmentImportForm',
    'NumberRoleForm',
)


class NumberImportForm(NetBoxModelImportForm):
    
    status = forms.ChoiceField(
        label=_('Status'),
        choices=NumberStatusChoices,
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
        queryset=Number.objects.all(),
        required=False
    )
    
    class Meta:
        model = Number
        fields = ('number', 'status','tenant','region', 'provider', 'forward_to', 'description', 'comments')
        
class NumberAssignmentImportForm(NetBoxModelImportForm):
    object_type = CSVContentTypeField(
        queryset=ContentType.objects.all(),
        help_text=_("One or more assigned object types")
    )
    number = DynamicModelChoiceField(
        queryset=Number.objects.all(),
        to_field_name='number',
        help_text=_('Assigned number')
    )
    role = DynamicModelChoiceField(
        queryset=NumberRole.objects.all(),
        to_field_name='name',
        help_text=_('Assigned role')
    )
    
    class Meta:
        model = NumberAssignment
        fields = ('object_type', 'object_id','number','role')

class NumberRoleImportForm(NetBoxModelImportForm):
    
    class Meta:
        model = NumberRole
        fields = ('name', 'description')