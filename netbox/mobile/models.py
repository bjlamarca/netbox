from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.text import slugify
from netbox.models import OrganizationalModel, PrimaryModel
from netbox.choices import ColorChoices
from utilities.fields import ColorField
from mobile.utils import format_phone
from mobile.choices import *



__all__ = (
    'MobileDeviceType',
    'MobileDeviceRole',
    'MobileDevice',
    'MobileNumber',
)

class MobileDeviceType(PrimaryModel):
       
    manufacturer = models.ForeignKey(
        to='dcim.Manufacturer',
        on_delete=models.PROTECT,
        related_name='mobile_device_types'
    )
    model = models.CharField(
        verbose_name=_('model'),
        max_length=100
    )
    part_number = models.CharField(
        verbose_name=_('part number'),
        max_length=50,
        blank=True,
        help_text=_('Discrete part number (optional)')
    )
    default_platform = models.ForeignKey(
        to='dcim.Platform',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
        verbose_name=_('default platform')
    )

    class Meta:
        ordering = ['manufacturer', 'model']
        constraints = (
            models.UniqueConstraint(
                fields=('manufacturer', 'model'),
                name='%(app_label)s_%(class)s_unique_manufacturer_model'
            ),
    )
        verbose_name = _('device type')
        verbose_name_plural = _('device types')

    def __str__(self):
        return self.model
    
    def get_absolute_url(self):
        return reverse('mobile:mobiledevicetype', args=[self.pk])

    @property
    def full_name(self):
        return f"{self.manufacturer} {self.model}"
    

class MobileDeviceRole(OrganizationalModel):
    
    color = ColorField(
        verbose_name=_('color'),
        default=ColorChoices.COLOR_GREY
    )
    
    class Meta:
        ordering = ('name',)
        verbose_name = ('device role')
        verbose_name_plural = ('device roles')

    def str(self):
        self.name
        

    def get_absolute_url(self):
        return reverse('mobile:mobiledevicerole', args=[self.pk])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
class MobileDevice(PrimaryModel):
    device_type = models.ForeignKey(
        to='mobile.MobileDeviceType',
        on_delete=models.PROTECT,
        related_name='instances'
    )
    role = models.ForeignKey(
        to='mobile.MobileDeviceRole',
        on_delete=models.PROTECT,
        related_name='mobile_devices',
        help_text=_("The function this device serves")
    )
    contact = models.ForeignKey(
        to='tenancy.Contact',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="mobile_device_set"
    )
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.PROTECT,
        related_name='mobile_devices',
        blank=True,
        null=True
    )
    platform = models.ForeignKey(
        to='dcim.Platform',
        on_delete=models.SET_NULL,
        related_name='mobile_devices',
        blank=True,
        null=True
    )
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=64,
        blank=True,
        null=True
    )
    serial = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_('serial number'),
        help_text=_("Serial number assigned by the manufacturer")
    )
    asset_tag = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        unique=True,
        verbose_name=_('asset tag'),
        help_text=_('A unique tag used to identify this device')
    )
    site = models.ForeignKey(
        to='dcim.Site',
        on_delete=models.PROTECT,
        related_name='mobile_devices',
        blank=True,
        null=True
    )
    location = models.ForeignKey(
        to='dcim.Location',
        on_delete=models.PROTECT,
        related_name='mobile_devices',
        blank=True,
        null=True
    )
    status = models.CharField(
        verbose_name=_('status'),
        max_length=50,
        choices=MobileDeviceStatusChoices,
        default=MobileDeviceStatusChoices.STATUS_ACTIVE
    )
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="mobile_device_tenant_set"

    )
    prerequisite_models = (
        'mobile.MobileDeviceRole',
        'mobile.MobileDeviceType',
    )
    class Meta:
        ordering = ('name', 'pk')  # Name may be null
        verbose_name = _('device')
        verbose_name_plural = _('devices')

    def __str__(self):
        if self.name and self.asset_tag:
            return f'{self.name} ({self.asset_tag})'
        elif self.name:
            return self.name
        elif self.device_type and self.asset_tag:
            return f'{self.device_type.manufacturer} {self.device_type.model} ({self.asset_tag})'
        elif self.device_type:
            return f'{self.device_type.manufacturer} {self.device_type.model} ({self.pk})'
        return super().__str__()

    def get_absolute_url(self):
        return reverse("mobile:mobiledevice", kwargs={"pk": self.pk})
    
    def get_status_color(self):
        return MobileDeviceStatusChoices.colors.get(self.status)
    
    

number_validator = RegexValidator(
    r"^\+?[0-9A-D\#\*]*$",
    "Numbers can only contain: leading +, digits 0-9; chars A, B, C, D; # and *"
)

class MobileNumber(PrimaryModel):
   
    number = models.CharField(max_length=32, validators=[number_validator])
    status = models.CharField(
        max_length=50,
        choices=MobileNumberStatusChoices,
        blank=False
    )
    contact = models.ForeignKey(
        to='tenancy.Contact',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="mobile_number_set"
    )
    device = models.ForeignKey(
        to='mobile.MobileDevice',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='mobile_number_set'
    )
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="mobile_number_set"

    )
    description = models.CharField(max_length=200, blank=True)
    provider = models.ForeignKey(
        to="circuits.Provider",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="mobile_number_set"
    )
    region = models.ForeignKey(
        to="dcim.Region",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="mobile_number_set"
    )
    forward_to = models.ForeignKey(
        to="mobile.MobileNumber",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="mobile_forward_to_set"
    )
    
    clone_fields = ('status', 'tenant', 'description', 'provider', 'region', 'forward_to')

    class Meta:
        ordering=('number',)
        verbose_name = _('mobile number')
        verbose_name_plural = _('mobile numbers')
        unique_together = ("number", "tenant",)

    def __str__(self):
        return str(format_phone(self.number))

    def get_absolute_url(self):
        return reverse("mobile:mobilenumber", kwargs={"pk": self.pk})
    
    def get_status_color(self):
        return MobileNumberStatusChoices.colors.get(self.status)

    def number_formatted(self):
        return format_phone(self.number)