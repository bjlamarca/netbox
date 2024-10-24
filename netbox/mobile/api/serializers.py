from django.utils.translation import gettext as _
from rest_framework import serializers

from mobile.choices import *
from mobile.models import *
from netbox.api.fields import ChoiceField, RelatedObjectCountField
from netbox.api.serializers import NetBoxModelSerializer
from dcim.api.serializers  import ManufacturerSerializer, PlatformSerializer, RegionSerializer
from circuits.api.serializers import ProviderSerializer
from tenancy.api.serializers_.tenants import TenantSerializer

__all__ = (
      'MobileMobileDeviceTypeSerializer',
      'MobileDeviceRoleSerializer',
      'MobileDeviceSerializer',
      'MobileNumberSerializer',
)

class MobileDeviceTypeSerializer(NetBoxModelSerializer):
    manufacturer = ManufacturerSerializer(nested=True)
    default_platform = PlatformSerializer(nested=True, required=False, allow_null=True)

    class Meta:
        model = MobileDeviceType
        fields = [
            'id', 'manufacturer', 'default_platform', 'model', 'part_number',
            'description', 'comments', 'tags', 'custom_fields',
            'created', 'last_updated',]
        
        brief_fields = ('id', 'manufacturer', 'model', 'description')

class MobileDeviceRoleSerializer(NetBoxModelSerializer):

    class Meta:
        model = MobileDeviceRole
        fields = [
            'id', 'name', 'color', 'description', 'tags', 'custom_fields', 'created', 'last_updated', 
        ]
        brief_fields = ('id', 'name', 'description',)

class MobileDeviceSerializer(NetBoxModelSerializer):
    device_type = MobileDeviceTypeSerializer(nested=True)
    role = MobileDeviceRoleSerializer(nested=True)
    tenant = TenantSerializer(
        nested=True,
        required=False,
        allow_null=True,
        default=None
    )
    platform = PlatformSerializer(nested=True, required=False, allow_null=True)
    status = ChoiceField(choices=MobileDeviceStatusChoices, required=False)

    class Meta:
        model = MobileDevice
        fields = [
            'id', 'name', 'role', 'device_type', 'tenant', 'platform', 'serial',
            'asset_tag', 'status', 'description', 'comments', 'tags', 'custom_fields', 'created', 'last_updated', 
        ]
        brief_fields = ('id', 'name', 'device_type', 'description')

class MobileNumberSerializer(NetBoxModelSerializer):
    status = ChoiceField(choices=MobileNumberStatusChoices, required=False)
    tenant = TenantSerializer(required=False, allow_null=True, nested=True)
    region = RegionSerializer(required=False, allow_null=True, nested=True)
    provider = ProviderSerializer(required=False, allow_null=True, nested=True)
    forward_to = serializers.PrimaryKeyRelatedField(queryset=MobileNumber.objects.all(), required=False, allow_null=True)

    
    class Meta:
        model = MobileNumber
        fields = [
            'id', 'number','status', 'tenant', 'region', 'forward_to', 'description', 'provider', 'tags',
        ]
        brief_fields = ('id', 'number','status')