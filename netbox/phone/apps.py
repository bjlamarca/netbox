from django.apps import AppConfig


class PhoneConfig(AppConfig):
    name = 'phone'
    verbose_name = "Phone"

    def ready(self) -> None:
        from phone.template_content import add_template_extensions
        from netbox.models.features import register_models
        from phone.navagation import add_to_menu
       
        
        register_models(*self.get_models())
        add_template_extensions()
        add_to_menu()
        
       
        