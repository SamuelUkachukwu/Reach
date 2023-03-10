from django.urls import path
from . import views


urlpatterns = [
    path('', views.wishes, name='wishes'),
    path('edit/<int:item_id>/', views.edit_wish, name='edit_wish'),
    path('delete/<int:item_id>/', views.delete_wish, name='delete_wish'),
]
