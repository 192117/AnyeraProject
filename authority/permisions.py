from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication


class IsUser(permissions.BasePermission):
    """
    Разрешение для пользователей.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated


class IsOwner(permissions.BasePermission):
    """
    Разрешение для хозяина питомца.
    """

    def has_permission(self, request, view):
        # Получаем авторизованного пользователя из JWT токена
        auth = JWTAuthentication()
        user_auth_tuple = auth.authenticate(request)
        if user_auth_tuple is not None:
            user, token = user_auth_tuple
        else:
            return False

        animal_user = view.queryset.filter(id=view.kwargs['pk']).values_list('user_id', flat=True)[0]

        # Проверяем, что пользователь аутентифицирован и имеет доступ к питомцу
        return user.is_authenticated and user.id == animal_user
