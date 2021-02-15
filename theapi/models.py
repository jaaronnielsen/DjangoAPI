from django.db import models

# Create your models here.
class Language(models.Model):
    Id = models.Field(primary_key = True)
    Name = models.CharField(max_length=60)

class Platform(models.Model):
    Id = models.Field(primary_key = True)
    Name = models.CharField(max_length=60)

class Technology(models.Model):
    Id = models.Field(primary_key = True)
    Name = models.CharField(max_length=60)

class Project(models.Model):
    Id = models.Field(primary_key = True)
    Title = models.CharField(max_length=60)
    Requirements = models.CharField(max_length=1000)
    Design = models.CharField(max_length=200)
    CompeltedDate = models.DateField

class ProjectLanguage(models.Model):
    Id = models.Field(primary_key = True)
    Project = models.ManyToManyField(Project)
    Language = models.ManyToManyField(Language)

class ProjectTechnology(models.Model):
    Id = models.Field(primary_key = True)
    Project = models.ManyToManyField(Project)
    Technology = models.ManyToManyField(Technology)

class ProjectPlatfrom(models.Model):
    Id = models.Field(primary_key = True)
    Project = models.ManyToManyField(Project)
    Platform = models.ManyToManyField(Platform)