from netbox.search import SearchIndex, register_search
from . import models


@register_search
class NumberIndex(SearchIndex):
    model = models.Number
    fields = (
        ('number', 100),
        ('tenant', 200),
        ('provider', 200),
        ('description', 500),
        ('comments', 5000),
    )
    display_attrs = ('number', 'tenant', 'region', 'provider', 'forward_to', 'description')