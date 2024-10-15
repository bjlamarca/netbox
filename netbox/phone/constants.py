from django.db.models import Q

NUMBERASSIGNMENT_OBJECT_TYPES = Q(
    Q(app_label='dcim', model__in=['device']) |
    Q(app_label='users', model__in=['user'])|
    Q(app_label='tenancy', model__in=['contact'])
)