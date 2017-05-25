from django.db import models

# Create your models here.


REGION = (
    ('city', 'city'),
    ('region', 'region'),
)


class Category(models.Model):
    name = models.CharField(max_length=250)
    translate = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=350)
    article_time = models.CharField(max_length=5)
    article_date = models.DateField()
    text = models.TextField()
    url = models.URLField()
    created_at = models.DateField(auto_now_add=True)
    latitude = models.DecimalField(
        max_digits=16, decimal_places=14, blank=True, null=True)
    longitude = models.DecimalField(
        max_digits=16, decimal_places=14, blank=True, null=True)
    category = models.ManyToManyField(Category, null=True, blank=True)
    region = models.CharField(
        max_length=15,
        choices=REGION,
        blank=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
