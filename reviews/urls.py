from django.urls import path
from .views import index
from graphene_django.views import GraphQLView

app_name = "reviews"

urlpatterns = [
    path("", index, name="index"),
    path("graphql", GraphQLView.as_view(graphiql=True)),
]
