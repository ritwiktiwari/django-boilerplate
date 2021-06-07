from rest_framework import status
from rest_framework.response import Response


def app_response(success=True, error=None, data=None, status_code=status.HTTP_200_OK):
    response = {
        "success": success,
        "error": error,
        "data": data
    }
    return Response(response, status=status_code)
