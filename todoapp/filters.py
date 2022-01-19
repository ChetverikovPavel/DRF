from dataclasses import field

from django_filters import rest_framework as filters
from pyexpat import model

from .models import Project


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="contains")

    class Meta:
        model = Project
        fields = ["name"]
