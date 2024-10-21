from django.utils.translation import gettext_lazy as _
from netbox.forms import NetBoxModelImportForm
from vault.models import *
from utilities.forms.fields import CSVModelChoiceField

__all__ = (
    'PasswordBulkImportForm',
    'PasswordRoleImportForm'
)

class PasswordBulkImportForm(NetBoxModelImportForm):

    role = CSVModelChoiceField(
        queryset=PasswordRole.objects.all(),
        to_field_name='name',
        help_text=_('Password role')
    )

    class Meta:
        model = Password
        fields = ('username', 'role','description', 'comments')

class PasswordRoleImportForm(NetBoxModelImportForm):
    
    class Meta:
        model = PasswordRole
        fields = ('name', 'description')
     

