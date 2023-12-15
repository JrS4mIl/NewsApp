from django.urls import path
from . import views

urlpatterns = [
    path('panel/manager/list',views.manager_list,name='manager_list'),
    path('panel/manager/del/<int:pk>',views.manager_delete,name='manager_delete'),
    path('panel/manager/group',views.manager_group,name='manager_group'),
    path('panel/manager/group/add',views.add_group,name='add_group'),
    path('panel/manager/group/del/<name>',views.manager_group_del,name='manager_group_del')

]
