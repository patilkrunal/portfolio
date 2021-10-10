from django.contrib import admin
from api.models import BasicInfo, Project, Experience, Education, Skill, Link, \
    Blog

# Register your models here.
admin.site.register(BasicInfo)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Link)
admin.site.register(Blog)
