from django.urls import path
from guest.views import GuestHelloView

urlpatterns = [
    path('guests/',GuestHelloView.as_view(),name='hello'),
]
