from django.contrib import admin
from .models import(
    Language,
    Platform,
    Project,
    ProjectLanguage,
    ProjectPlatfrom,
    ProjectTechnology,
    Technology
)
# Register your models here.
admin.site.register(Language)
admin.site.register(Technology)
admin.site.register(Platform)
admin.site.register(Project)
admin.site.register(ProjectLanguage)
admin.site.register(ProjectTechnology)
admin.site.register(ProjectPlatfrom)
