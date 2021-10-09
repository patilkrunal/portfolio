from django.urls import include, path
from rest_framework import routers

from api.views import ProjectViewSet, ExperienceViewSet, \
    EducationViewSet, SkillViewSet, LinkViewSet

router = routers.DefaultRouter()

router.register(r'projects', ProjectViewSet)
router.register(r'experience', ExperienceViewSet)
router.register(r'education', EducationViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'links', LinkViewSet)

urlpatterns = router.urls

