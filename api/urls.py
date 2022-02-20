from django.urls import include, path
from rest_framework import routers

from api.views import BasicInfoViewSet, ProjectViewSet, ExperienceViewSet, \
    EducationViewSet, SkillViewSet, LinkViewSet, BlogViewSet

router = routers.DefaultRouter()

router.register(r'basicinfo', BasicInfoViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'experience', ExperienceViewSet)
router.register(r'education', EducationViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'links', LinkViewSet)
router.register(r'blogs', BlogViewSet)

urlpatterns = router.urls

