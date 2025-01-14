
from django.contrib import admin
from django.urls import path, include

from api.views import UserCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),  # Accede a la URL base para usuarios

]

