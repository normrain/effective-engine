from django.urls import path
from Ticket.views import TicketApiDetail, TicketAPiList

urlpatterns = [
    path('<uuid:TicketID>/', TicketApiDetail.as_view(), name="api-ticket-detail"),
    path('', TicketAPiList.as_view(), name="ticket-api-list"),
]
