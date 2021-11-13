from rest_framework import viewsets, permissions
from .models import BasicInfo, Project, Experience, Education, Skill, Link, \
    Blog, Tag
from .serializers import \
    BasicInfoSerializer, ProjectSerializer, ExperienceSerializer, \
    EducationSerializer, SkillSerializer, LinkSerializer, BlogSerializer, \
    TagSerializer


class BasicInfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Basic Information to be created, viewed or modified
    """
    queryset = BasicInfo.objects.all()
    serializer_class = BasicInfoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Projects to be created, viewed or modified.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ExperienceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Experiences to be created, viewed or modified.
    """
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EducationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Education to be created, viewed or modified.
    """
    queryset = Education.objects.all().order_by('-end_date')
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SkillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Skills to be created, viewed or modified.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LinkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Links to be created, viewed or modified.
    """
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tags to be created, viewed or modified.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BlogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Links to be created, viewed or modified.
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
