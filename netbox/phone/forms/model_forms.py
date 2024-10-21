from django.utils.translation import gettext_lazy as _
from django import forms

from dcim.models import Device
from core.models import ObjectType
from netbox.forms import NetBoxModelForm
from phone.models import *
from phone.constants import *
from tenancy.models import Contact
from users.models import User
from utilities.forms.fields import CommentField, DynamicModelChoiceField, ContentTypeChoiceField
from utilities.forms.rendering import FieldSet, ObjectAttribute

__all__ = (
    'NumberForm',
    'NumberAssigmentForm'
    'NumberRoleForm',
)

class NumberForm(NetBoxModelForm):
    comments = CommentField()
    
    class Meta:
        model = Number
        fields = ('number', 'status','tenant', 'region', 'description', 'provider', 'forward_to', 'tags', 'comments')

class NumberAssignmentForm(NetBoxModelForm):
    
    object_type = ContentTypeChoiceField(
        label=_('Assigned Object'),
        queryset=ObjectType.objects.all(),
        limit_choices_to = NUMBERASSIGNMENT_OBJECT_TYPES,
        help_text=_("The object to assign this number to."),
        widget=forms.Select(attrs={"onChange": 'ShowTypeRelated();'})
    )
    users = DynamicModelChoiceField(
        label=_('User'),
        required=False,
        queryset=User.objects.all()
    )
    device = DynamicModelChoiceField(
        label=_('Device'),
        queryset=Device.objects.all(),
        required=False,
    )
    contacts = DynamicModelChoiceField(
        label=_('Contact'),
        queryset=Contact.objects.all(),
        required=False,
    )
    class Meta:
        model = NumberAssignment
        fields = ('object_type', 'users', 'device', 'contacts', 'number','role')
    def __init__(self, *args, **kwargs):

        # Initialize helper selectors
        instance = kwargs.get('instance')
        initial = kwargs.get('initial', {}).copy()
        print("Object", instance.object)
        if instance:
            if type(instance.object) is Device:
                initial['device'] = instance.object
            elif type(instance.object) is User:
                initial['users'] = instance.object
            elif type(instance.object) is Contact:
                initial['contacts'] = instance.object

        kwargs['initial'] = initial
        super().__init__(*args, **kwargs)


    def clean(self):
        super().clean()

        clean_object_type = self.cleaned_data.get('object_type')
        if clean_object_type.model_class() == User:
            print("USER")
            if not self.cleaned_data.get('users'):
                 raise forms.ValidationError("You must select a User")
            else:
                self.instance.object = self.cleaned_data.get('users')
        elif clean_object_type.model_class() == Device:
            if not self.cleaned_data.get('device'):
                 raise forms.ValidationError("You must select a Device")
            else:
                self.instance.object = self.cleaned_data.get('device')
        elif clean_object_type.model_class() == Contact:
            if not self.cleaned_data.get('contacts'):
                 raise forms.ValidationError("You must select a Contact")
            else:
                self.instance.object = self.cleaned_data.get('contacts')

        

class NumberRoleForm(NetBoxModelForm):
    
    class Meta:
        model = NumberRole
        fields = ('name', 'description', 'tags')



# fieldsets = (
    #     FieldSet(ObjectAttribute('object'), 'number', 'role'),
    #  )