from netbox.api.routers import NetBoxRouter
from . import views



router = NetBoxRouter()
router.APIRootView = views.PhonePluginRootView

router.register('numbers', views.NumberViewSet)
router.register('numberassignments', views.NumberAssignmentViewSet)
router.register('numberroles', views.NumberRoleViewSet)
#router.register(r'voice-circuits', views.VoiceCircuitsViewSet)

app_name = "phone-api"
urlpatterns = router.urls
