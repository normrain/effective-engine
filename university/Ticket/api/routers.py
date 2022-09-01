from rest_framework.routers import SimpleRouter
from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework_nested import routers

from Ticket.api.viewsets import TicketViewSet, ActivityViewSet

api_router = ExtendedSimpleRouter()
(
    api_router.register(r'tickets', TicketViewSet, basename='tickets')
    .register(r'activities',
              ActivityViewSet,
              basename='activities',
              parents_query_lookups=['ticket_id'],
              )
)

urlpatterns = api_router.urls

