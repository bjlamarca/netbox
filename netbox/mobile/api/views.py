from netbox.api.viewsets import NetBoxModelViewSet
from rest_framework.routers import APIRootView
from mobile.filtersets import *
from mobile.models import *
from . import serializers

class MobileRootView(APIRootView):
    """
    Mobile API root view
    """
    def get_view_name(self):
        return 'Mobile'
    
class MobileDeviceTypeViewSet(NetBoxModelViewSet):
    queryset = MobileDeviceType.objects.all()
    serializer_class = serializers.MobileDeviceTypeSerializer
    filterset_class = MobileDeviceTypeFilterSet

class MobileDeviceRoleViewSet(NetBoxModelViewSet):
    queryset = MobileDeviceRole.objects.all()
    serializer_class = serializers.MobileDeviceRoleSerializer
    filterset_class = MobileDeviceRoleFilterSet

class MobileDeviceViewSet(NetBoxModelViewSet):
    queryset = MobileDevice.objects.all()
    serializer_class = serializers.MobileDeviceSerializer
    filterset_class = MobileDeviceFilterSet

class MobileNumberViewSet(NetBoxModelViewSet):
    queryset = MobileNumber.objects.prefetch_related('tenant', 'region', 'tags')
    serializer_class = serializers.MobileNumberSerializer
    filterset_class = MobileNumberFilterSet
    