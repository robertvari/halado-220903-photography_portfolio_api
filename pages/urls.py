from django.urls import path

from .views import HomeView, SiteInfoView

urlpatterns = [
    path("", HomeView.as_view()),
    path("siteinfo/", SiteInfoView.as_view())
]