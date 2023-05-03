from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path(r'sign-up-player/',views.Sign_Up_Player),
    path(r'Login-Player/',views.Login_Player),
    path(r'Players-Profile-View/<str:id>/',views.Profile_view),
    path(r'Players-Profile-Edit/<str:id>/',views.Edit_Profile),
    
    path(r'Forgot-Password/',views.Forgot_Password),
    path(r'Otp-Verification/',views.Verify_otp),
    path(r'Forgot-change_password/',views.Forgot_change_password),
    path(r'change-new-password/<str:id>/',views.ChangePassword),
    
    path(r'Add_players/',views.Add_Game_Player),
    path(r'List_Of_Player/<str:id>/',views.List_Of_Player),
    path(r'View_Game_Player/',views.View_Game_Player),
    path(r'Edit_Game_Player/',views.Edit_Game_Player),
    path(r'Delete_Game_Player/',views.Delete_Game_Player),
    
    path(r'Spiner-List-Of-Player/<str:id>/',views.Spiner_List_Of_Player),
    path(r'Spiner-Drill-list/',views.Spiner_Drill_list),
    
    path(r'scoreboard-List/<str:id>/',views.Score_view),
    path(r'leaderboard-List/',views.Leaderboard_view),
    path(r'static-page-list/',views.Post_List),
    path(r'view-static-page-<str:id>/',views.Post_view),
    
    path(r'user-is-active-or-inactive/<str:id>/',views.User_Is_active),
    path(r'Contact-us-details/',views.Contact_Me),
    
    path(r'Drills-listing/',views.Drill_list),
    path(r'Drills-play-<str:id>/<str:last_num>/',views.Drill_Play),
    # path(r'Drill-play-calculator-<str:id>/',views.Drill_Calculator_Play),
    path(r'Drills-details-<str:id>/',views.Drill_formul),
    
    path(r'score-add/',views.Score_add),
    path(r'country-list/',views.country_list),
]