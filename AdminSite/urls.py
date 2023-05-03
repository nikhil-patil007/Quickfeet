from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('Login-Page/',views.Login,name="login"),
    path('Login/',views.Login_cr,name="Login_cr"),
    path('Logout/',views.Logout,name="Logout"),
    path('',views.Index_page,name='index'),
    path('All-Static-Pages-Table/',views.All_Static_Pages,name='Static_Pages'),
    path('All-Contact-Request-Table/',views.All_Request_Pages,name='All_Request_Pages'),
    
    path('All-Players-Table/',views.All_Player_Info,name='Player_Info'),
    path('Add-Players-Form/',views.Add_Player_form,name='Add_Player_form'),
    path('Add-Update-Players/',views.Add_Update_Player,name='Add_Update_Player'),
    path('Edit-Players-Form/<str:id>/',views.Edit_Player_form,name='Edit_Player_form'),
    path('Player-delete/<str:id>/',views.Delete_Player,name='delete_data'),
    
    path('Static-Page-form/',views.Add_Static_Form_Page,name='forms'),
    path('Static-Add-Update/',views.Add_Update_Static,name='Form_add'),
    path('Return-Reply/',views.Request_Reply,name='Request_Reply'),
    path('Drills-page/',views.Drills_List,name='all_drills_list'),

    path('Drills-Page-form/',views.Add_Drills_Form_Page,name='drills'),
    path('Drills-Add-form/',views.Drills_Add_Form,name='Drills_Add_Form'),
    
    
    path('Edit-<str:id>-drill-Page/',views.Edit_Drills_Form_Page,name='Edit_Drills_Form_Page'),
    path('Edit-<str:id>-Form-Page/',views.Edit_Static_Form_Page,name='Edit_Form_Page'),
    path('Request_view_page/<str:id>/',views.Request_Back,name='Request_Back'),
    path('static-delete/<str:id>/',views.static_delete,name='static_delete'),
    path('drills-delete/<str:id>/',views.Drills_delete,name='Drills_delete'),

    path('Game-User-Active-Inactive/',views.Game_User_Block,name='Game_User_Block'),
    path('Static-page-Publish/',views.Static_Publish,name='static_pages_js'),
    path('drills-status/',views.drills_Status,name='drills_Status'),
    path('lang-change-site/',views.lang_change,name='lang_change'),
]