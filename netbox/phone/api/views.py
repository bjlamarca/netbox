from netbox.api.viewsets import NetBoxModelViewSet
from rest_framework.routers import APIRootView
from phone.models import *
from phone.filtersets import *
from . import serializers

class PhoneRootView(APIRootView):
    """
    Phone API root view
    """
    def get_view_name(self):
        return 'Phone'
    
class NumberViewSet(NetBoxModelViewSet):
    queryset = Number.objects.prefetch_related('tenant', 'region', 'tags')
    serializer_class = serializers.NumberSerializer
    filterset_class = NumberFilterSet

class NumberAssignmentViewSet(NetBoxModelViewSet):
    queryset = NumberAssignment.objects.all()
    serializer_class = serializers.NumberSerializer
    filterset_class = NumberAssignmentFilterSet

class NumberRoleViewSet(NetBoxModelViewSet):
    queryset = NumberRole.objects.all()
    serializer_class = serializers.NumberRoleSerializer
    filterset_class = NumberRoleFilterSet


