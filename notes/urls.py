from django.urls import path

from .views import index, update_card, tags_list

urlpatterns = [
    path('', index, name='index'),
    path('update/<int:id>/', update_card, name='update_card'),
    path('tags/', tags_list, name='tags_list'),
    path('tags/<str:name>/', tags_list, name='tag_notes'),
]