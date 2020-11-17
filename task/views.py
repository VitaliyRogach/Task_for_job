from rest_framework.response import Response
from rest_framework import generics, status
from .models import Worker, Company
from .serializers import WorkerSerializer, CompanySerializer, AllInfSerializer
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


    def worker_list(self, request):
        queryset = self.get_queryset()
        serializer = WorkerSerializer(queryset, many=True)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        try:
            Worker.objects.filter(worker_position='Junior Python-Developer').delete()
            return HttpResponseRedirect("http://127.0.0.1:8000/api/workers/")
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CompanyView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAdminUser]

    def company_list(self, request):
        queryset = self.get_queryset()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)

# class AllInfView(generics.ListCreateAPIView):
#     def get(self, request, *args, **kwargs):
#         filters = {}
#         filters['model_1'] = Company.objects.all()
#         filters['model_2'] = Worker.objects.all()
#         serializer = AllInfSerializer(filters)
#         return Response(serializer.data)

# class AllInformationView(generics.ListCreateAPIView):
#     def querry(self, request):
#         workerSet = WorkerSerializer(Worker.objects.all())
#         companySet = CompanySerializer(Company.objects.all())
#         workerList = {}
#         companyList = {}
#         workerList = {
#                 "worker": [workerSet.data],
#         }
#         companyList = {
#                 "company": [companySet.data],
#         }
#         list={
#             "worker": [workerSet.data],
#             "company": [companySet.data]
#         }
#
#         return Response(list)