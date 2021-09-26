from django.urls import path

from .views import index, update_card, delete_card

urlpatterns = [
    path('', index, name='index'),
    path('update/<int:id>/', update_card, name='update_card'),
    path('delete/<int:id>/', delete_card, name='delete_card'),
]