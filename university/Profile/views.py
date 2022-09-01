from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
)

from django.contrib.auth.models import User
from IssueTracker.serializers import UserSerializer


class UserAPiList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserApiDetail(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = User
    lookup_field = "id"
