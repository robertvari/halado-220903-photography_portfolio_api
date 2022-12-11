from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from react.views import ReactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-v01/", include("pages.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path(r'', ReactView.as_view())
]