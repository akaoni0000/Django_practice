from django.urls import path
from . import views

app_name = "diary"
urlpatterns = [
    path("", views.index, name="index"),
    path("page/create/", views.page_create, name="page_create"),
    path("pages/", views.page_list, name="page_list"),
    path("page/<uuid:id>/", views.page_detail, name="page_detail"),#uuid型のデータ(id)が入る
    path("page/<uuid:id>/update/", views.page_update, name="page_update"),
    path("age/<uuid:id>/delete/", views.page_delete, name="page_delete"),

    path("user/login/", views.login, name="user_login"),
    path("user/home/", views.home, name="user_home"),
    path("user/logout/", views.logout, name="user_logout"),
    path("good/<uuid:id>", views.good, name="good"),
    path("good/delete/<uuid:id>", views.good_delete, name="good_delete"),


    path("user/test/", views.test, name="test_page"),
    path("user/test2/", views.test2, name="test2_page"),

    path("page/show/", views.page_show, name="page_show"),

    path("page/comment/", views.comment, name="comment"),
]