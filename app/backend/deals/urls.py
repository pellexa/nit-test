from django.urls import path
from . import views

urlpatterns = [
    path(
        'api/v1/deals/',
        views.get_post_deals,
        name='get_post_deals'
    ),
    path(
        'api/v1/deals/<int:id>/',
        views.get_delete_update_deal,
        name='get_delete_update_deal'
    ),
]
