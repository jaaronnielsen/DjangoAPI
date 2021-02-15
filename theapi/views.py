from django.shortcuts import render
from rest_framework import viewsets

from .models import(
    Language,
    Platform,
    Project,
    ProjectLanguage,
    ProjectPlatfrom,
    ProjectTechnology,
    Technology
)

from .serializers import(
    LanguageSerializer,
    PlatformSerializer,
    TechnologySerializer,
    ProjectSerializer,
    ProjectLanguageSerializer,
    ProjectPlatfromSerializer,
    ProjectTechnologySerializer
)

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all().order_by('Id')
    serializer_class = LanguageSerializer

class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all().order_by('Id')
    serializer_class = PlatformSerializer

class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all().order_by('Id')
    serializer_class = TechnologySerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('Id')
    serializer_class = ProjectSerializer