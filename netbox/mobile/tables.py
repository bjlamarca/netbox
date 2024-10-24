import django_tables2 as tables
from django_tables2.utils import Accessor
from django.utils.translation import gettext_lazy as _
from mobile.models import *
from netbox.tables import NetBoxTable, columns, ChoiceFieldColumn
from phone.utils import format_phone

__all__ = (
    'MobileDeviceTypeTable',
    'MobileDeviceRoleTable',
    'MobileDeviceTable',
    'MobileNumberTable',
)

#
# MobileDevice types
#

class MobileDeviceTypeTable(NetBoxTable):
    model = tables.Column(
        linkify=True,
        verbose_name=_('Device Type')
    )
    manufacturer = tables.Column(
        verbose_name=_('Manufacturer'),
        linkify=True
    )
    default_platform = tables.Column(
        verbose_name=_('Default Platform'),
        linkify=True
    )
    comments = columns.MarkdownColumn(
        verbose_name=_('Comments'),
    )
    tags = columns.TagColumn(
        url_name='mobile:devicetype_list'
    )
    class Meta(NetBoxTable.Meta):
        model = MobileDeviceType
        fields = (
            'pk', 'id', 'model', 'manufacturer', 'default_platform', 'description', 'comments', 'tags', 'created', 'last_updated',
        )
        default_columns = (
            'pk', 'model', 'manufacturer', 'part_number', 'u_height', 'is_full_depth', 'instance_count',
        )

class MobileDeviceRoleTable(NetBoxTable):
    name = tables.Column(
        verbose_name=_('Name'),
        linkify=True
    )
    device_count = columns.LinkedCountColumn(
        viewname='mobile:mobiledevice_list',
        url_params={'role_id': 'pk'},
        verbose_name=_('Devices')
    )
    color = columns.ColorColumn()
    # tags = columns.TagColumn(
    #     url_name='mobile:mobiledevicerole_list'
    # )

    class Meta(NetBoxTable.Meta):
        model = MobileDeviceRole
        fields = (
            'pk', 'id', 'name', 'device_count', 'color', 'description', 'tags', 'actions', 'created', 'last_updated',
        )
        default_columns = ('pk', 'name', 'device_count', 'color', 'description')

class MobileDeviceTable(NetBoxTable):
    name = tables.Column(
        verbose_name=_('Name'),
        order_by=('name',),
        linkify=True
    )
    status = columns.ChoiceFieldColumn(
        verbose_name=_('Status'),
    )
    manufacturer = tables.Column(
        verbose_name=_('Manufacturer'),
        accessor=Accessor('device_type__manufacturer'),
        linkify=True
    )
    device_type = tables.Column(
        linkify=True,
        verbose_name=_('Type')
    )
    role = columns.ColoredLabelColumn(
        verbose_name=_('Role')
    )
    platform = tables.Column(
        linkify=True,
        verbose_name=_('Platform')
    )
    comments = columns.MarkdownColumn()
    tags = columns.TagColumn(
        url_name='mobile:device_list'
    )

    class Meta(NetBoxTable.Meta):
        model = MobileDevice
        fields = ('pk', 'id', 'name', 'status', 'device_type', 'role', 'contact', 'tenant', 'manufacturer', 'serial', 'asset_tag', 'description', 'comments', 'tags', 'created', 'last_updated',)
        default_columns = ('pk', 'name', 'status', 'device_type', 'role', 'contact', 'tenant', 'manufacturer', )

class MobileNumberTable(NetBoxTable):

    id = tables.Column(
        linkify=True
    )
    status = ChoiceFieldColumn(
        verbose_name=_('Status'),
    )
    contact = tables.Column(
        linkify=True
    )
    device = tables.Column(
        linkify=True
    )
    number = tables.Column(
        verbose_name=_('Number'),
        linkify=True
    )
    forward_to = tables.Column(
        verbose_name=_('Forward To'),
        linkify=True,
    )
    tags = columns.TagColumn(
        url_name='phone:number_list'    
    )

    def render_number(self, value):
        return format_phone(value)
    
    class Meta(NetBoxTable.Meta):
        model = MobileNumber
        fields = ('id', 'number', 'status', 'contact', 'device', 'tenant', 'region', 'description', 'provider', 'forward_to', 'tags')
        default_columns = ('id', 'number', 'status', 'contact',  'device', 'group', 'tenant', 'region', 'description', 'provider', 'forward_to', 'tags')