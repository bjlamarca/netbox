from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError

class VaultConfig(AppConfig):
    name = 'vault'
    verbose_name = "Vault"

    def ready(self) -> None:
        #from phone.template_content import add_template_extensions
        from netbox.models.features import register_models
        from vault.navagation import add_to_menu
        from vault.template_content import add_template_extensions
       
        
        register_models(*self.get_models())
        add_template_extensions()
        add_to_menu()
        
        
       
        