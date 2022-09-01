from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
)


from Ticket.api.models import Ticket, Activity
from IssueTracker.serializers import TicketSerializer


# Create your views here.


class TicketApiDetail(RetrieveUpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_field = "TicketID"


class TicketAPiList(ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class ActivityApiDetail(RetrieveAPIView):
    queryset = Activity.objects.all()
    serializer_class = TicketSerializer
    lookup_field = "activityID"


class ActivityApiList(ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = TicketSerializer


