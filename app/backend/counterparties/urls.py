from django.urls import path
from . import views

urlpatterns = [
    path(
        'api/v1/counterparties/',
        views.get_post_counterparties,
        name='get_post_counterparties'
    ),
    path(
        'api/v1/counterparties/<int:id>/',
        views.get_delete_update_counterparty,
        name='get_delete_update_counterparty'
    ),
]
