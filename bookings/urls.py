from django.urls import path
from .views import RegisterView,LoginView,  BusListView, BusDetailView, BookingaView,UserBookingsView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('buses/', BusListView.as_view(), name='bus-list'),
    path('buses/<int:pk>/', BusDetailView.as_view(), name='bus-detail'),
    path('bookings/', BookingaView.as_view(), name='booking'),
    path('user/<int:user_id>/bookings',UserBookingsView.as_view(), name='user-bookings')
]