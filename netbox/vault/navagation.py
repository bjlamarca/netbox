from django.utils.translation import gettext_lazy as _
from netbox.choices import ButtonColorChoices
from netbox.registry import registry
from netbox.navigation import MenuGroup, Menu, get_model_item
from netbox.navigation.menu import ORGANIZATION_MENU, MENUS


    

    
VAULT_MENU = Menu(
    label=_('Vault'),
    icon_class='mdi mdi-lock',
    groups=(
        MenuGroup(
            label=_('Passwords'),
            items=(
                get_model_item('vault', 'password', _('Passwords')),
                get_model_item('vault', 'passwordrole', _('Password Roles')),
            ),
        ),
    ),
)

def add_to_menu():
    MENUS.insert(2,VAULT_MENU)
