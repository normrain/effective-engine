
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.response import Response

from django.contrib.auth.models import User, Group, Permission

from IssueTracker.serializers import UserSerializer, GroupSerializer, PermissionSerializer


class UserViewSet(NestedViewSetMixin, ModelViewSet):

    lookup_field = "id"
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(NestedViewSetMixin, ModelViewSet):

    lookup_field = "id"
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PermissionViewSet(NestedViewSetMixin, ModelViewSet):

    lookup_field = "id"
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class UserGroupViewSet(NestedViewSetMixin, ModelViewSet):
    lookup_field = "id"
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def list(self, request, parent_lookup_user__groups):
        user = User.objects.get(id=parent_lookup_user__groups)
        s_group = GroupSerializer(user.groups.all(), many=True)
        return Response(s_group.data)

    def retrieve(self, request,parent_lookup_user__groups, id):
        user = User.objects.get(id=parent_lookup_user__groups)
        group = user.groups.all().filter(id=id)
        s_group = GroupSerializer(group, many=True)
        return Response(s_group.data)
