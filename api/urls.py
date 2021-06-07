from django.urls import path

from .views import HealthCheckApi

urlpatterns = [
    path('health/', HealthCheckApi.as_view({
        'get': 'list',
    }), name="health"),
]
