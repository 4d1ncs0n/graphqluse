from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from graphene_django.views import GraphQLView
from products.schema import schema
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("reviews.urls", namespace="reviews")),
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
    path('products', views.products, name='products'),
]
