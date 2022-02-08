from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.do_logout, name="logout"),
    path("register/", views.do_register, name="register"),
    path("room/create/", views.create_room, name="create-room"),
    path("room/update/<str:pk>/", views.update_room, name="update-room"),
    path("room/delete/<str:pk>/", views.delete_room, name="delete-room"),
    path("room/<str:pk>/", views.room, name="room"),
    path("message/delete/<str:pk>/", views.delete_message, name="delete-message"),
    path("profile/update/", views.update_user, name="update-user"),
    path("profile/<str:pk>/", views.user_profile, name="user-profile"),
    path("topics/", views.topics, name="topics"),
    path("activity/", views.activity, name="activity"),
]
