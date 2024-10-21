
import logging
from django.db.utils import OperationalError
from django.contrib.contenttypes.models import ContentType
from netbox.plugins import PluginTemplateExtension, register_template_extensions

from .models import Password

logger = logging.getLogger(__name__)


panel_apps = {'tenancy.contact':'tab_view','tenancy.contact':'right_page'} #dict of apps to add panel to and location
template_extensions = []


def password_assignment_panel(self):
        obj = self.context['object']
        app_label, model = self.model.split('.')
        assigned_object_type = ContentType.objects.get(app_label=app_label, model=model).id

        return self.render('vault/inc/password_panel.html',
            extra_context={
                'passwords': Password.objects.filter(object_type=assigned_object_type, object_id=obj.id),
            })


def password_add_button(_app_model):
    class Button(PluginTemplateExtension):
        model = _app_model

        def buttons(self):
            return self.render(
                'vault/inc/password_add_button.html',
            )

    return Button

#Generate plugin extensions classes for each app, model
def add_template_extensions():
    try:
        for app, display in panel_apps.items():
            app_label, model = app.split('.')

            klass_name = f'{app_label}_{model}_plugin_template_extension'
            if display == 'tab_view':
                template_extensions.append(password_add_button(app))

            else:
                dynamic_klass = type(
                    klass_name,
                    (PluginTemplateExtension,),
                    {'model': app, display: password_assignment_panel},
                )
                template_extensions.append(dynamic_klass)
        
        register_template_extensions(template_extensions)
    except OperationalError as e:
        # This happens when the database is not yet ready
        logger.warning(f'Database not ready, skipping plugin extensions: {e}')
    except Exception as e:
        # Unexpected error
        raise Exception(f'Unexpected error: {e}')
