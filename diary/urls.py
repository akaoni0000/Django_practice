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
]