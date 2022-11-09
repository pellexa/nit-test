from django.urls import path
from . import views

urlpatterns = [
    path(
        'api/v1/deliverypoints/',
        views.get_post_deliveryPoints,
        name='get_post_deliveryPoints'
    ),
    path(
        'api/v1/deliverypoints/<int:id>/',
        views.get_delete_update_deliveryPoint,
        name='get_delete_update_deliveryPoint'
    ),
]
