from .serializers import DoctorSerializer
from rest_framework.views import APIView
from .models import Doctor
from rest_framework.response import Response

class DoctorList(APIView):

     def get(self, request):
         doctors =Doctor.objects.all()
         serializer = DoctorSerializer(doctors, many =True)
         return Response(serializer.data)

     def post(self):
         pass
