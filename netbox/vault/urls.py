from django.urls import include, path

from utilities.urls import get_model_urls
from . import views

app_name = 'vault'
urlpatterns = [

   # Passwords
    path('passwords/', views.PasswordListView.as_view(), name='password_list'),
    path('passwords/add/', views.PasswordEditView.as_view(), name='password_add'),
    path('passwords/import/', views.PasswordBulkImportView.as_view(), name='password_import'),
    path('passwords/edit/', views.PasswordBulkEditView.as_view(), name='password_bulk_edit'),
    path('passwords/delete/', views.PasswordBulkDeleteView.as_view(), name='password_bulk_delete'),
    path('passwords/<int:pk>/', include(get_model_urls('vault', 'password'))),

     #Password Role
     path('password-roles/', views.PasswordRoleListView.as_view(), name='passwordrole_list'),
     path('password-roles/add', views.PasswordRoleEditView.as_view(), name='passwordrole_add'),
     path('password-roles/import', views.PasswordRoleBulkImportView.as_view(), name='passwordrole_import'),
     path('password-roles/edit/', views.PasswordRoleBulkEditView.as_view(), name='passwordrole_bulk_edit'),
     path('password-roles/delete/', views.PasswordRoleBulkDeleteView.as_view(), name='passwordrole_bulk_delete'),
     path('password-roles/<int:pk>/', include(get_model_urls('vault', 'passwordrole'))),
     



]