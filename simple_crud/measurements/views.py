from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from measurements.serializers import ProjectSerializer, MeasurementSerializer
from measurements.models import Project, Measurement



class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

