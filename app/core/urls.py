from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

from .views import (HomeView, FlightListView, PassengerListView, FlightDetailView, FlightCreateView,
                    FlightUpdateView, AircraftListView, AircraftCreateView)

urlpatterns = [
        path('', HomeView.as_view(), name='index'),
        path('home/', HomeView.as_view(), name='index'),
        path('flights/', FlightListView.as_view(), name='flights'),
        path('passengers/', PassengerListView.as_view(), name='passengers'),
        # path('passengers/create', PassengerCreateView.as_view(), name='passengers_create'),
        path('flights/<int:pk>', FlightDetailView.as_view(), name='flight_detail'),
        path('flights/create', FlightCreateView.as_view(), name='flight_create'),
        path('flights/<int:pk>/update', FlightUpdateView.as_view(), name='flight_update'),
        path('aircrafts/', AircraftListView.as_view(), name='aircrafts'),
        path('aircrafts/create', AircraftCreateView.as_view(), name='aircraft_create'),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
