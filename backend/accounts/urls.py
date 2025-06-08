from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('my-profile/', views.my_profile, name="my-profile"),
    path('edit-profile/', views.edit_profile, name="edit-profile")
]