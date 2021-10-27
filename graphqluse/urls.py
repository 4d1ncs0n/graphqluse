from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from graphene_django.views import GraphQLView
from products.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("reviews.urls", namespace="reviews")),
    path("graphql", GraphQLViiew.as_view(graphiql=True, schema=schema)),
]
