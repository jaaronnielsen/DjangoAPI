from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Languages', views.LanguageViewSet)
router.register(r'Technology', views.TechnologyViewSet)
router.register(r'Platform', views.PlatformViewSet)
router.register(r'Project', views.ProjectViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
