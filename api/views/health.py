from rest_framework import viewsets

from api.common.utilities import app_response


class HealthCheckApi(viewsets.ViewSet):
    """
    Health Check Api
    Supported Methods: GET
    """

    def list(self, request):
        message = {
            "status": "Live"
        }
        return app_response(data=message)
