from rest_framework import serializers

from .models import(
    Language,
    Platform,
    Project,
    ProjectLanguage,
    ProjectPlatfrom,
    ProjectTechnology,
    Technology
)

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('Id', 'Name')

class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platform
        fields = ('Id', 'Name')

class TechnologySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Technology
        fields = ('Id', 'Name')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('Id', 'Title', 'Requirements', 'Design', 'CompletedDate')

class ProjectLanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectLanguage
        fields = ('Id', 'Project', 'Language')

class ProjectPlatfromSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectPlatfrom
        fields = ('Id', 'Project', 'Platform')

class ProjectTechnologySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectTechnology
        fields = ('Id', 'Project', 'Technology')