from netbox.forms import NetBoxModelFilterSetForm
from utilities.forms.fields import DynamicModelMultipleChoiceField, TagFilterField
from vault.models import *

__all__=[
    'PasswordFilterForm',
    'PasswordRoleFilterForm'
]

class PasswordFilterForm(NetBoxModelFilterSetForm):

    model = Password
    role = DynamicModelMultipleChoiceField(
        queryset=PasswordRole.objects.all(),
        required=False,
        label='Role',
    )

class PasswordRoleFilterForm(NetBoxModelFilterSetForm):
    model = PasswordRole
    tag = TagFilterField(model)
