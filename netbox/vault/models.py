from django.db import models
from django.urls import reverse
from netbox.models import OrganizationalModel, NetBoxModel, PrimaryModel
from django.contrib.contenttypes.fields import GenericForeignKey
from vault.crypto import encrypt, decrypt


class Password(PrimaryModel):
    object_type = models.ForeignKey(
        to='contenttypes.ContentType',
        on_delete=models.CASCADE
    )
    object_id = models.PositiveBigIntegerField()
    object = GenericForeignKey(
        ct_field='object_type',
        fk_field='object_id'
    )
    username = models.CharField(
        max_length=100,
        blank=False,
        verbose_name='User Name',

    )    
    ciphertext = models.BinaryField(
        max_length=65568,
        editable=False,  # 128-bit IV + 16-bit pad length + 65535B secret + 15B padding
    )
    role = models.ForeignKey(
        to='vault.PasswordRole',
        on_delete=models.PROTECT,
        related_name='password'
    )
    plaintext = '-----------'
    def password(self):
        if not self.ciphertext:
            return '---------'
        else:
            return '*********' 
   
    class Meta:
        ordering = ('pk',)
        verbose_name = ('password')
        verbose_name_plural = ('passwords')
    
    def __str__(self):
        return str(self.username)

    def get_absolute_url(self):
        return reverse("vault:password", kwargs={"pk": self.pk})
    
   

class PasswordRole(OrganizationalModel):
    """
   Type of password
    """
   
    class Meta:
        ordering = ('name',)
        verbose_name = ('password role')
        verbose_name_plural = ('password roles')
    
    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("vault:passwordrole", kwargs={"pk": self.pk})
    
    
