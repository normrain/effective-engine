from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
import datetime

from Ticket.api.models import Ticket, Activity
from IssueTracker.serializers import TicketSerializer, ActivitySerializer


class TicketViewSet(NestedViewSetMixin, ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    lookup_field = "ticket_id"
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def update(self, request, ticket_id):
        ticket = self.get_object()
        s_ticket = TicketSerializer(ticket, data=request.data)
        if s_ticket.is_valid(raise_exception=True):
            if s_ticket.validated_data['status'] == 'Closed':
                s_ticket.validated_data['closeDate'] = datetime.datetime.now()
            s_ticket.save()
            return Response(s_ticket.validated_data)
        else:
            return Response(s_ticket.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["GET"])
    def assigned(self, request):
        if not request.user.is_anonymous:
            ticket_list = Ticket.objects.filter(assignee=request.user)
            s_ticket_list = TicketSerializer(ticket_list, many=True)
            return Response(s_ticket_list.data)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=["HEAD", "GET", "PATCH"])
    def status(self, request, ticket_id):
        ticket = self.get_object()
        s_ticket = TicketSerializer(ticket, data=request.data, partial=True)
        if s_ticket.is_valid(raise_exception=True):
            if request.method in ("GET", "HEAD"):
                return Response({"status": s_ticket.data['status']})
            if request.method == "PATCH":
                if s_ticket.validated_data['status'] == 'Closed':
                    ticket.closeDate = datetime.datetime.now()
                s_ticket.save()
                return Response({"status": s_ticket.validated_data['status']})
        else:
            return Response(s_ticket.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivityViewSet(NestedViewSetMixin, ModelViewSet):
    lookup_field = "activity_id"
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def list(self, request, parent_lookup_ticket_id):
        queryset = Activity.objects.filter(ticket=parent_lookup_ticket_id).filter(external=True)
        s_activity_list = ActivitySerializer(queryset, many=True)
        return Response(s_activity_list.data)

    @action(detail=False, methods=["GET"])
    def all(self, request, parent_lookup_ticket_id):
        queryset = Activity.objects.filter(ticket=parent_lookup_ticket_id)
        s_activity_list = ActivitySerializer(queryset, many=True)
        return Response(s_activity_list.data)
