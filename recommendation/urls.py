from django.urls import path
from .views import RecommendBoxView

urlpatterns = [
    path(
        "",
        RecommendBoxView.as_view(),
        name="recommend-box"
    ),
]