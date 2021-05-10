from django.contrib import admin
from .models import Point, DATUMS
from django import forms


class PointForms(forms.ModelForm):
    model = Point
    fields = ['datums']


class PointAdmin(admin.ModelAdmin):
    form = PointForms


admin.site.register(Point, PointAdmin)
