from django.urls import path
from .views import DetailImageView, UpdateImageView


urlpatterns = [
    path('update-image/', UpdateImageView.as_view(), name='update-image'),
    path('update-image/<int:id>', DetailImageView.as_view(), name='detail-image'),
]
