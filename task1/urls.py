from django.urls import path

from .views import home, post_single

app_name = "task1"

urlpatterns = [
    path("", home, name="home"),
    path("single/<slug:post_slug>", post_single, name="post_single"),
]
