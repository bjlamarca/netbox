from django import forms
from core.models import ObjectType
from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField, ContentTypeChoiceField
from utilities.forms.rendering import FieldSet, ObjectAttribute
from vault.models import *
from vault.crypto import encrypt, decrypt

__all__ = (
    'PasswordForm',
    'PasswordRoleForm'
)

class PasswordForm(NetBoxModelForm):
    
    plaintext = forms.CharField(
        max_length=200,
        label='Password',
        
    )
    comments = CommentField()
    
    class Meta:
        model = Password
        fields = ('username', 'plaintext', 'role','description', 'comments')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.ciphertext:
            self.fields['plaintext'].initial = decrypt(self.instance.ciphertext)
      

    def clean(self):
        super().clean()
        
        if self.cleaned_data.get('plaintext'):
            cipher =  encrypt(self.cleaned_data.get('plaintext'))
            self.instance.ciphertext = cipher






class PasswordRoleForm(NetBoxModelForm):
    
    class Meta:
        model = PasswordRole
        fields = ('name', 'description', 'tags')