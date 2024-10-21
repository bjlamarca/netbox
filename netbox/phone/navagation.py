from django.utils.translation import gettext_lazy as _
from netbox.choices import ButtonColorChoices
from netbox.registry import registry
from netbox.navigation import MenuGroup, Menu, get_model_item
from netbox.navigation.menu import ORGANIZATION_MENU, MENUS


    

    
PHONE_MENU = Menu(
    label=_('Phone'),
    icon_class='mdi mdi-phone',
    groups=(
        MenuGroup(
            label=_('Phone'),
            items=(
                get_model_item('phone', 'number', _('Numbers')),
                get_model_item('phone', 'numberassignment', _('Number Assignments')),
                get_model_item('phone', 'numberrole', _('Number Roles')),
            ),
        ),
    ),
)

def add_to_menu():
    MENUS.insert(1,PHONE_MENU)
