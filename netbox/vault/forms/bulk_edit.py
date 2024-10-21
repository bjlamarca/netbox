from django import forms
from netbox.forms import NetBoxModelBulkEditForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from utilities.forms.rendering import FieldSet
from vault.models import *


__all__ = (
    'PasswordBulkEditForm',
    'PasswordRoleBulkEditForm'
)

class PasswordBulkEditForm(NetBoxModelBulkEditForm):

    role = DynamicModelChoiceField(
        label='Role',
        queryset=PasswordRole.objects.all(),
        required=False
    )
    description = forms.CharField(
        max_length=200,
        required=False
    )
    comments = CommentField()

    model = Password
    fieldsets = (
        FieldSet('role', 'description', 'comments')
    )
    nullable_fields = ('role', 'description', 'comments')

class PasswordRoleBulkEditForm(NetBoxModelBulkEditForm):
    description = forms.CharField(
        label='Description',
        max_length=200,
        required=False
    )

    model = PasswordRole
    fieldsets = (
        FieldSet('description'),
    )
    nullable_fields = ('description',)