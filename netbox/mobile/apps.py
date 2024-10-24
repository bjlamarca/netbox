from django.apps import AppConfig


class MobileConfig(AppConfig):
    name = 'mobile'
    verbose_name = "mobile"

    def ready(self) -> None:
        #from phone.template_content import add_template_extensions
        from netbox.models.features import register_models
        from mobile.navagation import add_to_menu
       
        
        register_models(*self.get_models())
        #add_template_extensions()
        add_to_menu()
        
       
        