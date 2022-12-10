from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class HomeView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response(
                {
                    "id": 123454,
                    "original_title": "Aliens",
                    "release_date": "1985-01-01"
                }
            )

class SiteInfoView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        return Response(
            {
                "name": "Robert Vari",
                "subtitle": "photography",
                "email": "robert@gmail.com"
            }
        )