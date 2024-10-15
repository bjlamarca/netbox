from django.utils.translation import gettext_lazy as _
import django_tables2 as tables

from .models import Number, VoiceCircuit, NumberAssignment, NumberRole
from django.conf import settings
from packaging import version

from netbox.tables import BaseTable, columns, NetBoxTable, ChoiceFieldColumn



class NumberTable(NetBoxTable):

    id = tables.Column(
        linkify=True
    )
    status = ChoiceFieldColumn(
        verbose_name=_('Status'),
    )
    number_formatted = tables.Column(
        verbose_name=_('Number'),
        linkify=True
    )
    forward_to = tables.Column(
        verbose_name=_('Forward To (BL)'),
        linkify=True,
    )
    tags = columns.TagColumn(
        url_name='phone:number_list'    
    )
    class Meta(BaseTable.Meta):
        model = Number
        fields = ('id', 'number_formatted', 'status', 'tenant', 'region', 'description', 'provider', 'forward_to', 'tags')
        default_columns = ('id', 'number_formatted', 'status', 'tenant', 'region', 'description', 'provider', 'forward_to', 'tags')

class NumberRoleTable(NetBoxTable):
    name = tables.Column(
        verbose_name=_('Name'),
        linkify=True
    )
    tags = columns.TagColumn()

    class Meta(NetBoxTable.Meta):
        model = NumberRole
        fields = ('id', 'name', 'description',  'tags', 'created', 'last_updated', 'actions')
        default_columns = ('id', 'name', 'description')

class NumberAssignmentTable(NetBoxTable):
    object_type = columns.ContentTypeColumn(
        verbose_name=_('Object Type')
    )
    object = tables.Column(
        verbose_name=_('Object'),
        linkify=True,
        orderable=False
    )
    number = tables.Column(
        verbose_name=_('Number'),
        linkify=True
    )
    # role = tables.Column(
    #     verbose_name=_('Role'),
    # )

    class Meta(NetBoxTable.Meta):
        model = NumberAssignment
        fields = ('id','object_type', 'object', 'number', 'role', 'description' )
        default_columns = ('id','object_type', 'object', 'number', 'role', 'description')

class VoiceCircuitTable(BaseTable):

    #id = ToggleColumn()
    name = tables.LinkColumn()
    voice_device_or_vm = tables.Column(
        accessor='assigned_object.parent_object',
        linkify=True,
        orderable=False,
        verbose_name='Device/VM'
    )
    voice_circuit_type = tables.LinkColumn()
    tenant = tables.LinkColumn()
    region = tables.LinkColumn()
    site = tables.LinkColumn()
    provider = tables.LinkColumn()
    tags = columns.TagColumn()

    class Meta(BaseTable.Meta):
        model = VoiceCircuit
        fields = ('id', 'name', 'voice_device_or_vm', 'voice_circuit_type', 'tenant', 'region', 'site', 'provider', 'tags')


class NumberAssignmentTable(NetBoxTable):
    object_type = columns.ContentTypeColumn(
        verbose_name=_('Object Type')
    )
    object = tables.Column(
        verbose_name=_('Object'),
        linkify=True,
        orderable=False
    )
    number = tables.Column(
        verbose_name=_('Number'),
        linkify=True
    )
    role = tables.Column(
        verbose_name=_('Role'),
        linkify=True
    )
    
    class Meta(NetBoxTable.Meta):
        model = NumberAssignment
        fields = ('id', 'object_type', 'object','number', 'role')
