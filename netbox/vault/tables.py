import django_tables2 as tables
from netbox.tables import NetBoxTable, columns, BaseTable
from vault.models import *

class PasswordTable(NetBoxTable):

    id = tables.Column(
        linkify=True
    )
    object_type = columns.ContentTypeColumn(
        verbose_name='Object Type'
    )
    object = tables.Column(
        verbose_name='Object',
        linkify=True,
        orderable=False
    )
    tags = columns.TagColumn(
        url_name='vault:password_list'    
    )
    class Meta(BaseTable.Meta):
        model = Password
        fields = ('pk', 'id', 'object_type', 'object', 'username', 'password', 'role', 'description' 'tags')
        default_columns = ('pk','id', 'object_type', 'object', 'username', 'password', 'role', 'description' 'tags')

class PasswordRoleTable(NetBoxTable):
    name = tables.Column(
        verbose_name='Name',
        linkify=True
    )
    tags = columns.TagColumn()

    class Meta(NetBoxTable.Meta):
        model = PasswordRole
        fields = ('id', 'name', 'description',  'tags', 'created', 'last_updated', 'actions')
        default_columns = ('id', 'name', 'description')