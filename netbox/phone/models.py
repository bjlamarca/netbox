from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from netbox.models import OrganizationalModel, NetBoxModel, PrimaryModel
from django.core.validators import RegexValidator
from phone.utils import format_phone

from django.urls import reverse
from .choices import VoiceCircuitTypeChoices, VOICE_CIRCUIT_ASSIGNMENT_MODELS, NumberStatusChoices

number_validator = RegexValidator(
    r"^\+?[0-9A-D\#\*]*$",
    "Numbers can only contain: leading +, digits 0-9; chars A, B, C, D; # and *"
)


class Number(PrimaryModel):
    """A Number represents a single telephone number of an arbitrary format.
    A Number can contain only valid DTMF characters and leading plus sign for E.164 support:
      - leading plus ("+") sign (optional)
      - digits 0-9
      - characters A, B, C, D
      - pound sign ("#")
      - asterisk sign ("*")
    Digit delimiters are now allowed. They will be implemented as a separate output formatter function.
    Number values can be not unique.
    Tenant is a mandatory option representing a number partition. Number and Tenant are globally unique.
    A Number can optionally be assigned with Provider and Region relations.
    A Number can contain an optional Description.
    A Number can optionally be tagged with Tags.
    """

    number = models.CharField(max_length=32, validators=[number_validator])
    status = models.CharField(
        max_length=50,
        choices=NumberStatusChoices,
        blank=False
    )
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    description = models.CharField(max_length=200, blank=True)
    provider = models.ForeignKey(
        to="circuits.Provider",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="provider_set"
    )
    region = models.ForeignKey(
        to="dcim.Region",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="region_set"
    )
    forward_to = models.ForeignKey(
        to="phone.Number",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="forward_to_set"
    )
    
    clone_fields = ('status', 'tenant', 'description', 'provider', 'region', 'forward_to')

    class Meta:
        ordering=('number',)
        verbose_name = _('number')
        verbose_name_plural = _('numbers')
        unique_together = ("number", "tenant",)

    def __str__(self):
        return str(format_phone(self.number))

    def get_absolute_url(self):
        return reverse("phone:number", kwargs={"pk": self.pk})
    
    def get_status_color(self):
        return NumberStatusChoices.colors.get(self.status)

    def number_formatted(self):
        return format_phone(self.number)
    
        

class NumberAssignment(NetBoxModel):
    object_type = models.ForeignKey(
        to='contenttypes.ContentType',
        on_delete=models.CASCADE
    )
    object_id = models.PositiveBigIntegerField()
    object = GenericForeignKey(
        ct_field='object_type',
        fk_field='object_id'
    )
    number = models.ForeignKey(
        to='phone.Number',
        on_delete=models.PROTECT,
        related_name='assignments'
    )
    role = models.ForeignKey(
        to='phone.NumberRole',
        on_delete=models.PROTECT,
        related_name='assignments'
    )


    class Meta:
        ordering = ('number',)
        indexes = (
            models.Index(fields=('object_type', 'object_id')),
        )
        verbose_name = _('number assignment')
        verbose_name_plural = _('number assignments')
    
    def __str__(self):
        return str(f"{self.number} -> {self.object}")

    def get_absolute_url(self):
        return reverse("phone:numberassignment", kwargs={"pk": self.pk})

class NumberRole(OrganizationalModel):
    """
    Functional role for a Number assigned to an object.
    """
    def get_absolute_url(self):
        return reverse('phone:numberrole', args=[self.pk])

    class Meta:
        ordering = ('name',)
        verbose_name = _('number role')
        verbose_name_plural = _('number roles')
    
    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("phone:numberrole", kwargs={"pk": self.pk})

class VoiceCircuit(NetBoxModel):
    """A Voice Circuit represents a single circuit of one of the following types:
    - SIP Trunk.
    - Digital Voice Circuit (BRI/PRI/etc).
    - Analog Voice Circuit (CO lines).
    """

    name = models.CharField(max_length=64)
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    description = models.CharField(max_length=200, blank=True)
    voice_circuit_type = models.CharField(
        max_length=50,
        choices=VoiceCircuitTypeChoices,
        blank=False
    )
    provider = models.ForeignKey(
        to="circuits.Provider",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="vc_provider_set"
    )
    provider_circuit_id = models.CharField(
        max_length=50,
        blank=True
    )
    region = models.ForeignKey(
        to="dcim.Region",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="vc_region_set"
    )
    site = models.ForeignKey(
        to="dcim.Site",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="vc_site_set"
    )
    
    sip_source = models.CharField(
        max_length=255,
        blank=True
    )
    sip_target = models.CharField(
        max_length=255,
        blank=True
    )

    assigned_object_type = models.ForeignKey(
        to=ContentType,
        limit_choices_to=VOICE_CIRCUIT_ASSIGNMENT_MODELS,
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True
    )
    assigned_object_id = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    assigned_object = GenericForeignKey(
        ct_field='assigned_object_type',
        fk_field='assigned_object_id'
    )

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("phone:voicecircuit", kwargs={"pk": self.pk})
