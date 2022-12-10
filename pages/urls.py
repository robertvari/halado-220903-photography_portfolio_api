from django.urls import path

from .views import SiteInfoView, AboutView, CategoryView, GalleryView, LandingPageView

urlpatterns = [
    path("siteinfo/", SiteInfoView.as_view()),
    path("about/", AboutView.as_view()),
    path("categories/", CategoryView.as_view()),
    path("gallery/", GalleryView.as_view()),
    path("landing-page/", LandingPageView.as_view())
]