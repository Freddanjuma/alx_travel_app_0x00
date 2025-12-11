from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Listings.
    Provides standard actions: list, create, retrieve, update, destroy.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Bookings.
    Provides standard actions: list, create, retrieve, update, destroy.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
