from django.urls import path, include

from .views import MyUserRegistrationView, MyUserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers


#добавить маршрутизаторы
router = routers.SimpleRouter()
router.register(r'', MyUserViewSet, basename='users')


urlpatterns = [
    path('register/', MyUserRegistrationView.as_view(), name='user-registration'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', include(router.urls)),
]