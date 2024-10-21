
from netbox.api.serializers import NestedGroupModelSerializer, NetBoxModelSerializer
from vault.models import *

class PasswordSerializer(NetBoxModelSerializer):

    #role = PasswordRoleSerializer(nested=True, required=False, allow_null=True)

    class Meta:
        model = Password
        fields = ('id','username', 'description', 'comments') #'role'
        brief_fields = ('id','username', 'description', 'comments')

class PasswordRoleSerializer(NetBoxModelSerializer):

    class Meta:
        model = PasswordRole
        fields = [
            'id', 'name', 'description', 'tags', 'custom_fields',
            'created', 'last_updated',
        ]
        brief_fields = ('id', 'name', 'slug', 'description')