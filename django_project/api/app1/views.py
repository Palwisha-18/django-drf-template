from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def home_view(request):
    """Returns successful response."""
    return Response({'healthy': True})
