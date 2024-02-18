import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .serializers import  historicalSerializers

class view_data(APIView):
    def get_API(self, resquest):
        api_url = "https://data.calgary.ca/resource/99yf-6c5u.json"

        try:
            response = requests.get(api_url)
            response.raise_for_status()
            
            serializer = historicalSerializers(data=response.json(), many=True)
            serializer.is_valid(raise_exception=True)

            return Response(serializer.data)
        
        except requests.exceptions.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
