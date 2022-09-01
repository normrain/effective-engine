from rest_framework.routers import SimpleRouter
from rest_framework_extensions.routers import ExtendedSimpleRouter

from Profile.api.viewsets import UserViewSet, GroupViewSet, PermissionViewSet, UserGroupViewSet

group_router = SimpleRouter()
group_router.register(r'groups', GroupViewSet, basename='groups')
permissions_router = SimpleRouter()
permissions_router.register(r'permissions', PermissionViewSet, basename='permissions')

user_router = ExtendedSimpleRouter()
(
    user_router.register(r'users', UserViewSet, basename='user')
        .register(r'groups',
                  UserGroupViewSet,
                  basename='user-groups',
                  parents_query_lookups=['user__groups'])

)
group_router = ExtendedSimpleRouter()
(
    group_router.register(r'groups',
                          GroupViewSet,
                          basename='groups')
        .register(r'permissions',
                  PermissionViewSet,
                  basename='groups-permissions',
                  parents_query_lookups=['group__permissions'])
)
user_permission_router = ExtendedSimpleRouter()
(
    user_permission_router.register(r'users', UserViewSet, basename='user')
        .register(r'permissions',
                  PermissionViewSet,
                  basename='users-permissions',
                  parents_query_lookups=['user__user_permissions'])
)

# new_urlpatterns = router.urls
profile_urlpatterns = user_router.urls + group_router.urls + user_permission_router.urls # + permissions_router.urls
