from netbox.api.routers import NetBoxRouter
from . import views

router = NetBoxRouter()
router.APIRootView = views.VaultRootView

router.register('passwords', views.PasswordViewSet)
router.register('passwordroles', views.PasswordRoleViewSet)

app_name = "vault-api"
urlpatterns = router.urls