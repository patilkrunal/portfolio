from django.db import models
from datetime import datetime, timedelta
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.urls import reverse
import itertools


class BasicInfo(models.Model):
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    caption_tags = models.CharField(max_length=200)
    description = models.TextField()
    about_title = models.CharField(max_length=200)
    about_description = models.TextField()
    profile_image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(blank=True)
    tech_stack = models.CharField(max_length=200)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    company_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    tech_stack = models.CharField(max_length=200)
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


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


DRAFT = 0
PUBLISHED = 1
FEATURED = 2
STATUS_CHOICES = (
    (DRAFT, 'Draft'),
    (PUBLISHED, 'Published'),
    (FEATURED, 'Featured')
)


class Blog(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300,
                            editable=False, unique=True)
    author = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField(
        config_name='awesome_ckeditor', null=True, blank=True)
    image_url = models.URLField(blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def is_recent(self):
        if self.created_on >= datetime.now() - timedelta(days=7):
            return True
        return False

    def _generate_slug(self):
        value = self.title
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not Blog.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)
        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        try:
            this_post = Blog.objects.get(id=self.id)
            if not self.pk and this_post.title != self.title:
                self._generate_slug()
        except:
            pass

        super(Blog, self).save(*args, **kwargs)

    def get_tags(self):
        return [t.name for t in self.tags.all()]

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('single-blog', kwargs=kwargs)
