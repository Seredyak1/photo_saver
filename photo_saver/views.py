from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
    schema,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(["GET"])
@schema(None)
# @authentication_classes([])
@permission_classes([AllowAny,])
def simple_health_check(request):
    return Response()
