from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from django import forms
from leaflet.forms.fields import PointField
from leaflet.forms.widgets import LeafletWidget

# Register your models here.
from master.scraping.models import Article

class YourMapWidget(LeafletWidget):
    geometry_field_class = 'YourGeometryField'


class PersonForm(forms.ModelForm):
    leaflet = PointField()

    class Media:
        js = [
        'vendor/jquery/jquery.js',
            'jquery.init.js',
        ]


    class Meta:
        model = Article
        fields = '__all__'
        widget={'leaflet': YourMapWidget()}


class AuthorAdmin(LeafletGeoAdmin):
        form = PersonForm


admin.site.register(Article, AuthorAdmin)
