
from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.UserCreateView.as_view(), name='user-create'),
    path('create-soup/', views.SoupCreateView.as_view(), name='create-soup'),
    path('sopas/<int:user_id>', views.UserSoupListView.as_view(), name='user-soups'),
    path('sopas/<int:user_id>/<int:soup_id>/', views.UserSoupDetailView.as_view(), name='user-soup-detail'),


]
