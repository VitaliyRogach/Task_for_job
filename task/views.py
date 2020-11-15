from rest_framework.response import Response
#from rest_framework.views import APIView
from rest_framework import generics, status
from .models import Worker, Company
from .serializers import WorkerSerializer, CompanySerializer
from rest_framework.permissions import IsAdminUser
from django.http import Http404
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound



class WorkersView(generics.ListCreateAPIView):
    #filter by work_position
    #queryset = Worker.objects.filter(worker_position='.Net Developer')
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = WorkerSerializer(queryset, many=True)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        try:
            Worker.objects.filter(worker_position='Junior Python-Developer').delete()
            return HttpResponseRedirect("http://127.0.0.1:8000/api/workers/")
        except:
            return Response(list, status=status.HTTP_404_NOT_FOUND)


class CompanyView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)

