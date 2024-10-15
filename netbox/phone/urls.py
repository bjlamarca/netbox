from django.urls import path, include
from phone import views
from phone.models import Number, NumberAssignment, NumberRole
from netbox.views.generic import ObjectChangeLogView
from utilities.urls import get_model_urls


app_name = 'phone'

urlpatterns = [
    #Numbers
    path('numbers/', views.NumberListView.as_view(), name='number_list'),
    path('numbers/add', views.NumberEditView.as_view(), name='number_add'),
    path('numbers/import', views.NumberBulkImportView.as_view(), name='number_import'),
    path('numbers/edit/', views.NumberBulkEditView.as_view(), name='number_bulk_edit'),
    path('numbers/delete/', views.NumberBulkDeleteView.as_view(), name='number_bulk_delete'),
    path('numbers/<int:pk>/', include(get_model_urls('phone', 'number'))),
    path('numbers/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='number_changelog', kwargs={
         'model': Number
    }),
    #Number Assignment
     path('number-assignments/', views.NumberAssignmentListView.as_view(), name='numberassignment_list'),
     path('number-assignments/add', views.NumberAssignmentEditView.as_view(), name='numberassignment_add'),
     path('number-assignments/import', views.NumberAssignmentBulkImportView.as_view(), name='numberassignment_import'),
     path('number-assignments/edit/', views.NumberAssignmentBulkEditView.as_view(), name='numberassignment_bulk_edit'),
     path('number-assignments/delete/', views.NumberAssignmentBulkDeleteView.as_view(), name='numberassignment_bulk_delete'),
     path('number-assignments/<int:pk>/', include(get_model_urls('phone', 'numberassignment'))),
     path('number-assignments/test/', views.NumberAssignmentTestView.as_view(), name='numberassignment_test'),
     path('number-assignments/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='numberassignment_changelog', kwargs={
          'model': NumberAssignment
     }),
     #Number Role
     path('number-roles/', views.NumberRoleListView.as_view(), name='numberrole_list'),
     path('number-roles/add', views.NumberRoleEditView.as_view(), name='numberrole_add'),
     path('number-roles/import', views.NumberRoleBulkImportView.as_view(), name='numberrole_import'),
     path('number-roles/edit/', views.NumberRoleBulkEditView.as_view(), name='numberrole_bulk_edit'),
     path('number-roles/delete/', views.NumberRoleBulkDeleteView.as_view(), name='numberrole_bulk_delete'),
     path('number-roles/<int:pk>/', include(get_model_urls('phone', 'numberrole'))),
     path('number-roles/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='numberrole_changelog', kwargs={
          'model': NumberRole
     }),
]