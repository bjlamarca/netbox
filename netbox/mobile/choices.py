from utilities.choices import ChoiceSet
from django.utils.translation import gettext_lazy as _

class MobileNumberStatusChoices(ChoiceSet):
    AVAILABLE = 'available'
    ASSIGNED = 'assigned'
    UNKNOWN = 'unknown'
    INACTIVE = 'inactive'
    CHOICES = (
        (AVAILABLE, 'Available', 'green' ),
        (ASSIGNED, 'Assigned', 'blue'),
        (UNKNOWN, 'Unknown', 'red'),
        (INACTIVE, 'Inactive', 'grey')
    )

class MobileDeviceStatusChoices(ChoiceSet):
    key = 'Device.status'

    STATUS_OFFLINE = 'offline'
    STATUS_ACTIVE = 'active'
    STATUS_PLANNED = 'planned'
    STATUS_STAGED = 'staged'
    STATUS_FAILED = 'failed'
    STATUS_INVENTORY = 'inventory'
    STATUS_DECOMMISSIONING = 'decommissioning'
    STATUS_DECOMMISSIONED = 'decommissioned'

    CHOICES = [
        (STATUS_OFFLINE, _('Offline'), 'gray'),
        (STATUS_ACTIVE, _('Active'), 'green'),
        (STATUS_PLANNED, _('Planned'), 'cyan'),
        (STATUS_STAGED, _('Staged'), 'blue'),
        (STATUS_FAILED, _('Failed'), 'red'),
        (STATUS_INVENTORY, _('Inventory'), 'purple'),
        (STATUS_DECOMMISSIONING, _('Decommissioning'), 'yellow'),
        (STATUS_DECOMMISSIONED, _('Decommissioned'), 'black'),
    ]