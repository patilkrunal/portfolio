import graphene
from graphene_django import DjangoObjectType
from api.models import BasicInfo, Project, Experience, Education, Skill, Link, \
    Blog


class BasicInfoType(DjangoObjectType):
    class Meta: 
        model = BasicInfo
        fields = "__all__"


class ProjectType(DjangoObjectType):
    class Meta: 
        model = Project
        fields = "__all__"


class ExperienceType(DjangoObjectType):
    class Meta: 
        model = Experience
        fields = "__all__"


class EducationType(DjangoObjectType):
    class Meta: 
        model = Education
        fields = "__all__"


class SkillType(DjangoObjectType):
    class Meta: 
        model = Skill
        fields = "__all__"


class LinkType(DjangoObjectType):
    class Meta: 
        model = Link
        fields = "__all__"


class BlogType(DjangoObjectType):
    class Meta: 
        model = Blog
        fields = "__all__"



class Query(graphene.ObjectType):
    basicinfo = graphene.List(BasicInfoType)
    projects = graphene.List(ProjectType)
    experiences = graphene.List(ExperienceType)
    education = graphene.List(EducationType)
    skill = graphene.List(SkillType)
    link = graphene.List(LinkType)
    blog = graphene.List(BlogType)

    def resolve_basicinfo(root, info, **kwargs):
        return BasicInfo.objects.all()

    def resolve_projects(root, info, **kwargs):
        return Project.objects.all()

    def resolve_experiences(root, info, **kwargs):
        return Experience.objects.all()

    def resolve_basicinfo(root, info, **kwargs):
        return Education.objects.all()

    def resolve_projects(root, info, **kwargs):
        return Skill.objects.all()

    def resolve_experiences(root, info, **kwargs):
        return Link.objects.all()
        
    def resolve_experiences(root, info, **kwargs):
        return Blog.objects.all()


schema = graphene.Schema(query=Query)
