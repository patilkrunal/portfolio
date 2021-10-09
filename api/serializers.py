from abc import ABC

from rest_framework import serializers
from api.models import Project, Experience, Education, Skill, Link


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"

