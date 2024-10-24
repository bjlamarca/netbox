from django.urls import path, include
from mobile import views
from mobile.models import *
from utilities.urls import get_model_urls

app_name = 'mobile'

urlpatterns = [

     # Device types
    path('mobiledevice-types/', views.MobileDeviceTypeListView.as_view(), name='mobiledevicetype_list'),
    path('mobiledevice-types/add/', views.MobileDeviceTypeEditView.as_view(), name='mobiledevicetype_add'),
    path('mobiledevice-types/import/', views.MobileDeviceTypeImportView.as_view(), name='mobiledevicetype_import'),
    path('mobiledevice-types/edit/', views.MobileDeviceTypeBulkEditView.as_view(), name='mobiledevicetype_bulk_edit'),
    path('mobiledevice-types/delete/', views.MobileDeviceTypeBulkDeleteView.as_view(), name='mobiledevicetype_bulk_delete'),
    path('mobiledevice-types/<int:pk>/', include(get_model_urls('mobile', 'mobiledevicetype'))),

    # Device roles
    path('mobiledevice-roles/', views.MobileDeviceRoleListView.as_view(), name='mobiledevicerole_list'),
    path('mobiledevice-roles/add/', views.MobileDeviceRoleEditView.as_view(), name='mobiledevicerole_add'),
    path('mobiledevice-roles/import/', views.MobileDeviceRoleBulkImportView.as_view(), name='mobiledevicerole_import'),
    path('mobiledevice-roles/edit/', views.MobileDeviceRoleBulkEditView.as_view(), name='mobiledevicerole_bulk_edit'),
    path('mobiledevice-roles/delete/', views.MobileDeviceRoleBulkDeleteView.as_view(), name='mobiledevicerole_bulk_delete'),
    path('mobiledevice-roles/<int:pk>/', include(get_model_urls('mobile', 'mobiledevicerole'))),

    # Devices
    path('mobiledevices/', views.MobileDeviceListView.as_view(), name='mobiledevice_list'),
    path('mobiledevices/add/', views.MobileDeviceEditView.as_view(), name='mobiledevice_add'),
    path('mobiledevices/import/', views.MobileDeviceBulkImportView.as_view(), name='mobiledevice_import'),
    path('mobiledevices/edit/', views.MobileDeviceBulkEditView.as_view(), name='mobiledevice_bulk_edit'),
    path('mobiledevices/rename/', views.MobileDeviceBulkRenameView.as_view(), name='mobiledevice_bulk_rename'),
    path('mobiledevices/delete/', views.MobileDeviceBulkDeleteView.as_view(), name='mobiledevice_bulk_delete'),
    path('mobiledevices/<int:pk>/', include(get_model_urls('mobile', 'mobiledevice'))),

    #Numbers
    path('mobilenumbers/', views.MobileNumberListView.as_view(), name='mobilenumber_list'),
    path('mobilenumbers/add', views.MobileNumberEditView.as_view(), name='mobilenumber_add'),
    path('mobilenumbers/import', views.MobileNumberBulkImportView.as_view(), name='mobilenumber_import'),
    path('mobilenumbers/edit/', views.MobileNumberBulkEditView.as_view(), name='mobilenumber_bulk_edit'),
    path('mobilenumbers/delete/', views.MobileNumberBulkDeleteView.as_view(), name='mobilenumber_bulk_delete'),
    path('mobilenumbers/<int:pk>/', include(get_model_urls('mobile', 'mobilenumber'))),
    


]