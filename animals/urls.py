from django.urls import path

from animals.views import AnimalCreateView, AnimalsDetailView, AnimalsListView

urlpatterns = [
    path('animals/', AnimalsListView.as_view(), name='animals'),
    path('animals/create/', AnimalCreateView.as_view(), name='create_new_animal'),
    path('animals/<int:pk>/', AnimalsDetailView.as_view(), name='get_delete_update_animal'),
]
