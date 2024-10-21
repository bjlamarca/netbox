from netbox.api.viewsets import NetBoxModelViewSet
from rest_framework.routers import APIRootView
from vault.models import *
from vault.filtersets import *
from . import serializers

class VaultRootView(APIRootView):
    """
    Vault API root view
    """
    def get_view_name(self):
        return 'Vault'
    
class PasswordViewSet(NetBoxModelViewSet):
    queryset = Password.objects.prefetch_related('role')
    serializer_class = serializers.PasswordSerializer
    filterset_class = PasswordFilterSet

class PasswordRoleViewSet(NetBoxModelViewSet):
    queryset = PasswordRole.objects.all()
    serializer_class = serializers.PasswordRoleSerializer
    filterset_class = PasswordRoleFilterSet