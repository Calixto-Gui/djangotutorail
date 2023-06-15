from django.urls import path

from . import views
from .views import create_post, add_comment

app_name = 'blog'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("create.post", create_post, name="create.post"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:post_id>/add_comment", add_comment, name="add_comment"),
]