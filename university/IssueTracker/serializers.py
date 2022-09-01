from rest_framework.serializers import ModelSerializer

from Ticket.api.models import Ticket, Activity, Tag
from django.contrib.auth.models import User, Group, Permission


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"





class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        groups = validated_data['groups']
        permissions = validated_data['user_permissions']
        user = User.objects.create_user(username, email, password)
        user.save()
        user.groups.add(*groups)
        user.user_permissions.add(*permissions)
        return user

class GroupSerializer(ModelSerializer):

    class Meta:
        model = Group
        fields = "__all__"

class TicketSerializer(ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Ticket
        fields = "__all__"
        depth = 1


class ActivitySerializer(ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"


class PermissionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"
