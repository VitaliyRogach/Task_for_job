from rest_framework import serializers
from .models import Worker, Company

class WorkerSerializer(serializers.Serializer):
    worker_name = serializers.CharField(max_length=120)
    worker_position = serializers.CharField()
    worker_age = serializers.CharField()

    def create(self, validated_data):
        return Worker.objects.create(**validated_data)


class CompanySerializer(serializers.Serializer):

    company_name = serializers.CharField(max_length=120)

    def create(self, validated_data):
        return Company.objects.create(**validated_data)

# class AllInfSerializer(serializers.Serializer):
#     model_2 = WorkerSerializer(read_only=True, many=True)
#     model_1 = CompanySerializer(read_only=True)
#
#     def create(self, validated_data):
#         return Company.objects.create(**validated_data)
