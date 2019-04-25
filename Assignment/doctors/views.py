from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Doctor,Availability
from .serializers import DoctorSerializer,AvailableSerializer


class DoctorList(APIView):
    """
    List all snippets, or create a new snippet.
    """


    def get(self, request, format=None):
        snippets = Doctor.objects.all()
        serializer = DoctorSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AvailList(APIView):
    """
    List all snippets, or create a new snippet.
    """


    def get(self, request, format=None):
        snippets = Availability.objects.all()
        serializer = AvailableSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = AvailableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)