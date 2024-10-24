from django.utils.translation import gettext_lazy as _
from netbox.choices import ButtonColorChoices
from netbox.registry import registry
from netbox.navigation import MenuGroup, Menu, get_model_item
from netbox.navigation.menu import ORGANIZATION_MENU, MENUS


    

    
MOBILE_MENU = Menu(
    label=_('Mobile Devices'),
    icon_class='mdi mdi-cellphone',
    groups=(
        MenuGroup(
            label=_('Mobile'),
            items=(
                get_model_item('mobile', 'mobilenumber', _('Numbers')),
                get_model_item('mobile', 'mobiledevice', _('Devices')),
                get_model_item('mobile', 'mobiledevicetype', _('Device Types')),
                get_model_item('mobile', 'mobiledevicerole', _('Device Roles')),
            ),
        ),
    ),
)

def add_to_menu():
    MENUS.insert(1,MOBILE_MENU)
