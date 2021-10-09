from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(blank=True)
    # tech_stack = models.CharField(max_length=200)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    company_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    # tech_stack = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.company_name
    

class Education(models.Model):
    school_name = models.CharField(max_length=200)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.school_name


class Skill(models.Model):
    name = models.CharField(max_length=200)
    priority = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.name


class Link(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    icon_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

