from netbox.api.routers import NetBoxRouter
from . import views



router = NetBoxRouter()
router.APIRootView = views.MobileRootView

router.register('device-types', views.MobileDeviceTypeViewSet)
router.register('device-roles', views.MobileDeviceRoleViewSet)
router.register('devices', views.MobileDeviceViewSet)
router.register('numbers', views.MobileNumberViewSet)


app_name = "mobile-api"
urlpatterns = router.urls