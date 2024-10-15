from django.utils.translation import gettext_lazy as _
from core.models import ObjectType
from netbox.forms import NetBoxModelFilterSetForm
from phone.models import Number, NumberAssignment, NumberRole
from utilities.forms.fields import DynamicModelMultipleChoiceField, TagFilterField, ContentTypeMultipleChoiceField
from utilities.forms.rendering import FieldSet
from dcim.models import Region
from tenancy.models import Tenant
from circuits.models import Provider


class NumberFilterForm(NetBoxModelFilterSetForm):

    model = Number
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
    provider_id = DynamicModelMultipleChoiceField(
        queryset=Provider.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
    )
    tag = TagFilterField(model)

class NumberAssignmentFilterForm(NetBoxModelFilterSetForm):
    model = NumberAssignment
    # fieldsets = (
    #     FieldSet('q', 'filter_id', 'tag'),
    #     FieldSet('object_type', 'object', 'number', 'role', 'description'),
    # )
    object_type = ContentTypeMultipleChoiceField(
        queryset=ObjectType.objects.with_feature('contacts'),
        required=False,
        label=_('Object type')
    )
    number = DynamicModelMultipleChoiceField(
        queryset=Number.objects.all(),
        required=False,
        label=_('Number')
    )
    role = DynamicModelMultipleChoiceField(
        queryset=NumberRole.objects.all(),
        required=False,
        label=_('Role')
    )
    tag = TagFilterField(model)

class NumberRoleFilterForm(NetBoxModelFilterSetForm):
    model = NumberRole
    tag = TagFilterField(model)