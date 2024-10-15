from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError

class PhoneConfig(AppConfig):
    name = 'phone'
    verbose_name = "Phone"

    def ready(self) -> None:
        from phone.template_content import add_template_extensions
        from netbox.models.features import register_models
        register_models(*self.get_models())
        add_template_extensions()

        