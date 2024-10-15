from rest_framework import serializers
from phone.models import *
from phone.choices import NumberStatusChoices
from netbox.api.serializers import NestedGroupModelSerializer, NetBoxModelSerializer
from netbox.api.fields import ChoiceField, ContentTypeField
from tenancy.api.serializers import TenantSerializer
from dcim.api.serializers import RegionSerializer, SiteSerializer
from circuits.api.serializers import ProviderSerializer

class NumberSerializer(NetBoxModelSerializer):
    status = ChoiceField(choices=NumberStatusChoices, required=False)
    tenant = TenantSerializer(required=True, allow_null=False, nested=True)
    region = RegionSerializer(required=False, allow_null=True, nested=True)
    provider = ProviderSerializer(required=False, allow_null=True, nested=True)
    forward_to = serializers.PrimaryKeyRelatedField(queryset=Number.objects.all(), required=False, allow_null=True)

    
    class Meta:
        model = Number
        fields = [
            'id', 'number','status', 'tenant', 'region', 'forward_to', 'description', 'provider', 'tags',
        ]
        brief_fields = ('id', 'number','status')

class NumberRoleSerializer(NetBoxModelSerializer):

    class Meta:
        model = NumberRole
        fields = [
            'id', 'name', 'description', 'tags', 'custom_fields',
            'created', 'last_updated',
        ]
        brief_fields = ('id', 'name', 'slug', 'description')

class NumberAssignmentSerializer(NetBoxModelSerializer):
    object_type = ContentTypeField(
        queryset=ContentType.objects.all()
    )
    number = NumberSerializer(nested=True, required=False, allow_null=True)
    role = NumberRoleSerializer(nested=True, required=False, allow_null=True)
    class Meta:
        model = NumberAssignment
        fields = [
            'object_type', 'object_id','number','role'
        ]
        brief_fields = ('id', 'number','status')








