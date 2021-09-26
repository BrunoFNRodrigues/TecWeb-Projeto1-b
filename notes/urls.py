from django.urls import path

from .views import index, update_card

urlpatterns = [
    path('', index, name='index'),
    path('update/<int:id>/', update_card, name='update_card'),
]